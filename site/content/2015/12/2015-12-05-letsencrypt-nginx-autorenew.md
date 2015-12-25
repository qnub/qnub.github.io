Title: Автообновление сертификатов Let's Encrypt для Nginx
Date: 2015-12-05 18:00:00
Category: it  
Tags: ssl, https, letsencrypt, nginx
Author: qnub  
Image: /images/it/letsencrypt.png
Slug: 2015-12-05-letsencrypt-nginx-autorenew


[Let's Encrypt](https://letsencrypt.org/) перешёл в стадию публичной беты, а значит каждый может заполучить себе халявные SSL сертификаты для веба. Одно но — пока они очень короткоиграющие (3 месяца) потому рекомендуется замутить себе их автообновление раз в 2 месяца.

В один сертификат можно вписать 2 домена. На домен вторго уровня можно получить сертификаты только на 2 домена. Другими словами на каждый домен второго уровня можно сделать халявное шифрование для него самого и одного поддомена или для 2х поддоменов, но не для него самого… Про большую вложенность не знаю, как и про *«wildcard»* домены. Надеюсь будут позже.

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

    listen [::]:443 ssl spdy;
    listen 443 ssl spdy; # we enable SPDY here

    ssl on;

    ssl_certificate /etc/letsencrypt/live/<full_domain_name>/cert.pem;
    ssl_certificate_key /etc/letsencrypt/live/<full_domain_name>/privkey.pem;
    ssl_trusted_certificate /etc/letsencrypt/live/<full_domain_name>/chain.pem;

    ssl_stapling on;
    ssl_stapling_verify on;  
    ssl_session_timeout 5m;
    ssl_session_cache shared:SSL:10m;

    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;
    ssl_ciphers 'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!3DES:!MD5:!PSK';

    add_header Strict-Transport-Security "max-age=63072000;";

Не забывая заменить в путях `<full_domain_name>` на имя домена использованного в перменной `$MAIN_DOMAIN` скрипта автообновления.

Ну и можно сделать редирект с `http` на `https`:

    server {
        server_name <domain_name>;

        location / {
            rewrite     ^ https://$server_name$request_uri? permanent;
        }
    }

`<domain_name>` — имя домена для редиректа. Собственно конфиги (и редиректы) `nginx` надо не забыть обновить во всех файлах (если ваши домены в разных файлах). Если у вас нет не зашифрованных серверов — имеет смысл указать редирект на дефолтном сервере…

В данный момент этот скрипт и сертификаты я уже спользую в своих сайтах, в том числе <https://www.registr.xyz>.
