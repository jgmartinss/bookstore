from django.contrib import admin

from . import models


class OrderItemAdmin(admin.ModelAdmin):
    model = models.OrderItem
    ordering = ("-created",)
    search_fields = ("order__user__email", "product__title")
    list_display = ("order", "product", "quantity", "price", "created")
    list_display_links = ["order"]
    date_hierarchy = "created"


class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
    raw_id_fields = ["product"]


class OrderAdmin(admin.ModelAdmin):
    save_on_top = True
    save_as = True
    list_per_page = 15
    ordering = ("-created",)
    list_display = ["id", "user", "status", "created"]
    list_filter = ["status", "created"]
    search_fields = ("user__email",)
    list_display_links = ["user"]
    date_hierarchy = "created"
    inlines = [OrderItemInline]
    fieldsets = (
        (
            "Add order",
            {"fields": (("user", "status"), "shipping_address", "billing_address")},
        ),
    )


admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderItem, OrderItemAdmin)
