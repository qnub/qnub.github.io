Title: Автообновление сертификатов Let's Encrypt для Nginx
Date: 2015-12-05 18:00:00
Category: it  
Tags: ssl, https, letsencrypt, nginx
Author: qnub  
Image: /images/it/letsencrypt.png
Slug: 2015-12-05-letsencrypt-nginx-autorenew


[Let's Encrypt](https://letsencrypt.org/) перешёл в стадию публичной беты, а значит каждый может заполучить себе халявные SSL сертификаты для веба. Одно но — пока они очень короткоиграющие (3 месяца) потому рекомендуется замутить себе их автообновление раз в 2 месяца.

В один сертификат можно вписать 2 домена.

Для начала нужно клонировать репозиторий с утилитой `letsencrypt`:

    git clone https://github.com/letsencrypt/letsencrypt

Вот вам работающий (на данный момент) скрипт для автообновления сертификатов <https://gist.github.com/qnub/ce475a5007db1d9b04d8>.

В скрипте надо прописать:

    EMAIL=user@example.org  # ваш емайл для связи
    LETSENCRYPT=/root/letsencrypt  # путь к клонированному репозиторию letsencrypt
    MAIN_DOMAIN=example.com  # освноной домен сертификата
    SECOND_DOMAIN=example.org  # дополнительный домен сертификата


Скрипт забиваете в крон от рута на запуск раз в 2 месяца (старт 03:02 1го числа каждого второго месяца):

    02 03 01 */2 * /<path_to>/renew-letsencrypt.sh

Для работы утилиты требуется 80 порт, так что скрипт остановит `nginx` обновит сертификаты и запустит его снова (ждём плагин для nginx который позволит не отключать сервер для обновления).

Остаётся в настройках домена `nginx` прописать что-то вроде:

    ssl on;

    ssl_certificate /etc/letsencrypt/live/<full_domain_name>/cert.pem;
    ssl_certificate_key /etc/letsencrypt/live/<full_domain_name>/privkey.pem;
    ssl_trusted_certificate /etc/letsencrypt/live/<full_domain_name>/fullchain.pem;

    ssl_stapling on;
    ssl_stapling_verify on;  
    ssl_session_timeout 5m;
    ssl_session_cache shared:SSL:10m;

    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;
    ssl_ciphers 'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!3DES:!MD5:!PSK';

Не забывая заменить в путях `<full_domain_name>` на имя домена использованного в перменной `$MAIN_DOMAIN` скрипта автообновления.

В данный момент этот скрипт и сертификаты я уже спользую в своих сайтах, в том числе <https://www.registr.xyz>.
