from django.utils.translation import gettext_lazy as _


ORDER_STATUS = (
    (1, _("Processing")),
    (2, _("Pending Payment")),
    (3, _("Canceled")),
    (4, _("Complete")),
    (5, _("Billed")),
)
