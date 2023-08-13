from django.contrib import admin

from .models import Users


class UsersAdmin(admin.ModelAdmin):
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
