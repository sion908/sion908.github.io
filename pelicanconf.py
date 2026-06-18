AUTHOR = '紫苑'
SITENAME = 'プログラマーの手帳'
SITEURL = ""
SITENAME = 'My Tech Blog'
SITEDESCRIPTION = '技術メモや学習記録を残すブログ'
OG_LOCALE = 'ja_JP'

PATH = "content"

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'
THEME = 'themes/mnmlist'
STATIC_PATHS = ['static']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_OG_IMAGE = 'https://sion908.github.io/images/default_ogp.jpg'

TWITTER_USERNAME = 'sion908'  # @は不要

# Blogroll
LINKS = [
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
]

# Social widget
SOCIAL = [
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


STATIC_PATHS = ['extra', 'images']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
}

PLUGINS = ['sitemap']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.7,
        'indexes': 0.5,
        'pages': 0.3,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    },
}

