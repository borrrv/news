from rest_framework import serializers
from news.models import News, Comments


class CommentSerializer(serializers.ModelSerializer):
    """Сериалайзер для комментариев"""
    class Meta:
        model = Comments
        fields = (
            "id",
            "news",
            "text",
            "pub_date",
        )


class NewsSerializer(serializers.ModelSerializer):
    """Сериалайзер для новостей"""
    author = serializers.ReadOnlyField(source="author.username")
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "text",
            "author",
            "pub_date",
            "comments",
        )
