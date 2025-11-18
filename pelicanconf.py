AUTHOR = 'patrickD'
SITENAME = 'patrickD'

SITEURL = ""
FEED_DOMAIN = "https://patrickd.xyz"
PAGE_URL = "pages/{slug}"
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}.html'
CATEGORY_URL = 'category/{slug}/'
TAG_URL = 'tag/{slug}'

THEME = "theme/notmyidea"
PATH = "content"

TIMEZONE = 'MST'

DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'
DEFAULT_CATEGORY = 'posts'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (
#     ("Pelican", "https://getpelican.com/"),
#     ("Jinja2", "https://palletsprojects.com/p/jinja/"),
# )

# Social widget

# if true, adds minimal hcard to social links
# currently hardcoded into base.html in notmyidea template.
SOCIAL_HCARD = True
SOCIAL = (
    ("LinkedIn", "https://www.linkedin.com/in/patrick-dornian/"),
    ("GitHub", "https://github.com/pdornian"),

)

DEFAULT_PAGINATION = 25

DELETE_OUTPUT_DIRECTORY = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
