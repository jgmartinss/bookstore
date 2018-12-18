from django.utils.translation import gettext_lazy as _


VISIBLE_WHERE = (
    (1, _('Catalog')),
    (2, _('Search')),
    (3, _('Catalog, Search')),
)

SHOW_REAL_PRICE = (
    (1, _('In cart')),
    (2, _('Search')),
    (3, _('Before confirming order')),
)

AVAILABILITY_OF_STOCK = (
    (1, _('Out of stock')),
    (2, _('In stock')),
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

NUMBER_OF_STAR = (
    (1, _('1 Star')),
    (2, _('2 Star')),
    (3, _('3 Star')),
    (4, _('4 Star')),
    (5, _('5 Star')),
)