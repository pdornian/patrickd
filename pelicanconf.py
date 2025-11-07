AUTHOR = 'patrickD'
SITENAME = 'patrickD'
SITEURL = "https://patrickd.xyz"

THEME = "theme/notmyidea"
PATH = "content"

TIMEZONE = 'MST'

DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
)

# Social widget

# if true, adds minimal hcard to social links
# currently hardcoded into base.html in notmyidea template.
SOCIAL_HCARD = True
SOCIAL = (
    ("LinkedIn", "https://www.linkedin.com/in/patrick-dornian/"),
    ("GitHub", "https://github.com/pdornian"),

)

DEFAULT_PAGINATION = 25

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
