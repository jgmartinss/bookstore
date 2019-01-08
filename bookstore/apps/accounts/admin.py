from django.contrib import admin

from . import models


class UserAdmin(admin.ModelAdmin):
    model = models.User
    ordering = ("email", "-created")
    search_fields = ("email",)
    list_display = ("email", "is_superuser", "is_admin", "is_active", "created")
    list_display_links = ["email"]
    list_filter = ("is_active", "is_superuser", "is_admin")
    date_hierarchy = "created"
    fieldsets = (
        ("Account info", {"fields": ("email", "password")}),
        (
            "Permissions and status",
            {"fields": (("is_active", "is_superuser", "is_admin"),)},
        ),
        (
            "Customer info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "phone_number",
                    "tax_vat_number",
                    "company",
                    ("gender", "birthday"),
                )
            },
        ),
    )


class AddressAdmin(admin.ModelAdmin):
    model = models.Address
    ordering = ("user__first_name", "-created")
    search_fields = ("user__email", "postal_code")
    list_display = ("postal_code", "streets_in_line", "region_in_line")
    list_display_links = ["postal_code"]
    list_filter = ("is_billing_address",)
    date_hierarchy = "created"


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Address, AddressAdmin)
