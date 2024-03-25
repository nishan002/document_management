from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('id','email', 'name', 'is_admin')
    list_display_links = ('email', 'name')
    ordering = ['id','email']

    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'name', 'password1', 'password2'),
    }),
)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, AccountAdmin)