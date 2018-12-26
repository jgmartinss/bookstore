from django.utils.translation import gettext_lazy as _


CATALOG = 1
SEARCH = 2
CATALOG_SEARCH = 3

VISIBLE_WHERE = (
    (CATALOG, _('Catalog')),
    (SEARCH, _('Search')),
    (CATALOG_SEARCH, _('Catalog, Search')),
)

INCART = 1
SEARCH = 2
BEFOREORDER = 3

SHOW_REAL_PRICE = (
    (INCART, _('In cart')),
    (SEARCH, _('Search')),
    (BEFOREORDER, _('Before confirming order')),
)

OFSTOCK = 1
INSTOCK = 2

AVAILABILITY_OF_STOCK = (
    (OFSTOCK, _('Out of stock')),
    (INSTOCK, _('In stock')),
)

ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5

NUMBER_OF_STAR = (
    (ONE, _('1 Star')),
    (TWO, _('2 Star')),
    (THREE, _('3 Star')),
    (FOUR, _('4 Star')),
    (FIVE, _('5 Star')),
)

LANGUAGES = [
    ('bg', _('Bulgarian')),
    ('cs', _('Czech')),
    ('de', _('German')),
    ('en-us', _('English')),
    ('es', _('Spanish')),
    ('fa-ir', _('Persian (Iran)')),
    ('fr', _('French')),
    ('hu', _('Hungarian')),
    ('it', _('Italian')),
    ('ja', _('Japanese')),
    ('ko', _('Korean')),
    ('nb', _('Norwegian')),
    ('nl', _('Dutch')),
    ('pl', _('Polish')),
    ('pt-br', _('Portuguese (Brazil)')),
    ('ro', _('Romanian')),
    ('ru', _('Russian')),
    ('sk', _('Slovak')),
    ('tr', _('Turkish')),
    ('uk', _('Ukrainian')),
    ('vi', _('Vietnamese')),
    ('zh-hans', _('Chinese')),
    ('zh-tw', _('Chinese (Taiwan)'))
]
