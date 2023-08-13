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
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "text",
            "author",
            "pub_date",
            "likes_count",
            "comments_count",
            "comments",
        )

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_comments_count(self, obj):
        return obj.comments.count()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        last_comments = instance.comments.order_by("-pub_date")[:10]
        comments_serializer = CommentSerializer(last_comments, many=True)
        representation["comments"] = comments_serializer.data
        return representation
