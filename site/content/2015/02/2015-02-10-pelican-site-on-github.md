Title: Бесплатный хостинг на GitHub блога, сгенерированного Pelican  
Date: 2015-02-10 15:00:00 
Category: blog  
Tags: github, static, pelican  
Author: qnub  
Image: /images/blog/pelican.png
Slug: 2015-02-10-pelican-site-on-github

Исходник этого самого блога можно найти на [GitHub](https://github.com/qnub/qnub.github.io/tree/master). Здесь немного модифицирован `Makefile` для поддержки `virtualenv` находящегося в каталоге `.env` в каталоге с, собственно, `git` самого сайта. Тема разработана [temapavloff](https://github.com/temapavloff), а дизайн [yahujik](https://ru.linkedin.com/in/yahujik/ru). И то и другое немного изменено и, и то и другое в оригинале используется в нашем совместном проекте [gik.me подкаст](http://gik.me).

Я добавил обственную версию генератора RSS который поддерживает мультимедиа аттачи (для подкаста) и в самой теме активно используются мета-данные из статей для генерации правильных [Open Graph](http://ogp.me/) тегов.

Дополнительные опции в конфигурации **Pelican**:

    :::python
    from filters import cat_name

    JINJA_FILTERS = {
        'cat_name': cat_name,  # позволяет выводить в темплейте руссифицированные имена категорий
    }

    # карта преобразования имён категорий для вышеприведённого фильтра
    CATEGORY_MAP = {
        'link': u'ссылки',
        'quote': u'цитаты',
        'text': u'текст',
        'blog': u'блог',
        'news': u'новости',
        'article': u'статьи',
    }

    # перенос в корень сайта нужных статических файлов при генерации
    # CNAME содержит собственный домен сайта для использования с GitHub Pages
    STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.png', 'extra/favicon.ico', 'extra/CNAME']
    EXTRA_PATH_METADATA = {
        'extra/robots.txt': {'path': 'robots.txt'},
        'extra/favicon.ico': {'path': 'favicon.ico'},
        'extra/favicon.png': {'path': 'favicon.png'},
        'extra/CNAME': {'path': 'CNAME'},
    }

    PLUGINS = ['feeds_with_media', ]  # сосбтвенно плагин, герерирующий более правильный RSS

    # дополнительные данные для вышеприведённого плагина
    FEED_IMAGE = '/favicon.png'  # картинка фида
    FEED_FOOTER = ''  # футер с копирайтом добавляется если пост в фиде содержит медиа-вложение

Сам генератор RSS берёт информацию для вложения из мета-тегов. Если у статьи указан тег `Encolsure:` то ссылка из этого тега будет добавлена в пост фида как ссылка на вложение, а `MIME-type` из тега `Mime:` будет использован для указания типа этого вложения.

Также тема поддерживает эти мета-теги добавляет соотвествующие `og:` мета-теги в `<head>` страницы. Туда же будет добавлен линк на картинку, если указан тег `Image:`.
