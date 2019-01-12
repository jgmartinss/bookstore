from django.contrib import admin

from bookstore.apps.newsletter.models import Subscribe


class SubscribeAdmin(admin.ModelAdmin):
    model = Subscribe
    list_per_page = 20
    date_hierarchy = "created"
    ordering = ("full_name", "-created")
    search_fields = ("full_name", "email", "created_by")
    list_display = ("email", "full_name", "created_by", "created")
    list_display_links = ["email"]
    fieldsets = ((None, {"fields": (("email", "full_name"), "created_by")}),)


admin.site.register(Subscribe, SubscribeAdmin)
