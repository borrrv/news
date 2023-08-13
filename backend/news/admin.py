from django.contrib import admin

from .models import Comments, News


class NewsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "pub_date",
    )
    list_filter = (
        "id",
        "title",
        "author",
    )
    search_fields = (
        "title",
    )


class CommentsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
        "news",
        "pub_date",
    )
    list_filter = (
        "id",
        "author",
        "news",
    )


admin.site.register(News, NewsAdmin)
admin.site.register(Comments, CommentsAdmin)
