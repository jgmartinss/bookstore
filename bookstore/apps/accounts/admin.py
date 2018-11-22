from django.contrib import admin

from . import models


class UserAdmin(admin.ModelAdmin):
    model = models.User
    ordering = ('email', '-created',)
    search_fields = ('email',)
    list_display = ('email', 'is_superuser', 'is_active', 'created')
    list_display_links = ['email']
    list_filter = ('is_active',)
    date_hierarchy = 'created'
    fieldsets = (
        ('Account info', {
            'fields': ('email', 'password')
        }),
        ('Permissions and status', {
            'fields': (('is_active', 'is_superuser', 'is_admin'),)
        }),
        ('Customer info', {
            'fields': (
                'first_name', 'last_name',
                'phone_number', 'tax_vat_number',
                'company', ('gender', 'birthday',),
            )
        }),
    )

admin.site.register(models.User, UserAdmin)
