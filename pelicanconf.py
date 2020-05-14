#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'choutos'
SITENAME = 'choutos'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Vienna'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa"
}

# Blogroll
#LINKS = (('Linkedin', 'https://www.linkedin.com/in/victor-andrade-a020a415/'),
#         ('Twitter', 'https://twitter.com/choutos'),)
#         ('Twitter', 'https://twitter.com/choutos'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('Linkedin', 'https://www.linkedin.com/in/victor-andrade-a020a415/'),
#          ('Another social link', '#'),)
SOCIAL = (
    ('linkedin', 'https://www.linkedin.com/in/victor-andrade-a020a415/'),
    ('twitter', 'https://twitter.com/choutos'),
    ('github', 'https://github.com/choutos'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = 'Flex'
