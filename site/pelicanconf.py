#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys

sys.path.append(os.curdir)

from filters import cat_name

JINJA_FILTERS = {
    'cat_name': cat_name,
}

AUTHOR = u'qnub'
SITENAME = u"qnub's blog"
SITEURL = 'http://qnub.me'

PATH = 'content'

TIMEZONE = 'Asia/Omsk'

DEFAULT_LANG = u'ru_RU'

STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.png', 'extra/favicon.ico', 'extra/CNAME']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/favicon.png': {'path': 'favicon.png'},
    'extra/CNAME': {'path': 'CNAME'},
}

ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
PLUGINS = ['feeds_with_media', ]

THEME = './themes/qnub'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_MAX_ITEMS = 15
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'blog'
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DELETE_OUTPUT_DIRECTORY = True

SUMMARY_MAX_LENGTH = 30
PAGE_ORDER_BY = 'order'

DEFAULT_PAGINATION = 10

RELATIVE_URLS = True
TYPOGRIFY = True

FEED_IMAGE = '/favicon.png'
FEED_FOOTER = ''
CATEGORY_MAP = {
    'link': u'ссылки',
    'quote': u'цитаты',
    'text': u'текст',
    'blog': u'блог',
    'news': u'новости',
    'it': u'IT',
    'game': u'игры',
    'article': u'статьи'
}

# MENUITEMS = (
#     ('news', '/category/news.html', u'Новости'),
# )

# DISQUS_SITENAME = ""
