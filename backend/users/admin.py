from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Users


class UsersAdmin(UserAdmin):
    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
    )
    list_filter = (
        'email',
        'username',
    )
    search_fields = (
        'username',
    )


admin.site.register(Users, UsersAdmin)
