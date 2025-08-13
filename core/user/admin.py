from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.utils.translation import gettext as _


class UserAdmin(BaseUserAdmin):
    ordering = ('lastname', 'firstname')
    list_display = ['id','email', 'lastname', 'firstname',]
    search_fields = ('id', 'email', 'lastname', 'firstname')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {
            'fields': ('lastname', 'firstname')}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'lastname', 'firstname', 'password')
        }),
    )
admin.site.register(User, UserAdmin)