from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from rest_auth.models import User
# Register your models here.

class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'username')
    list_filter = ('email', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username',)}),
        ('Permissions', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        })
    )
    ordering = ('email',)
    search_fields = ('email', 'username')


admin.site.register(User, UserAdmin)
