from users.authentication import CustomAuthentication
from rest_framework.viewsets import ModelViewSet
from news.models import News, Comments
from .serializers import NewsSerializer, CommentSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from .permissions import IsAuthorOrAdmin
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED


class GetAuthToken(ObtainAuthToken):
    authentication_classes = [CustomAuthentication]


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all().select_related('author')
    serializer_class = NewsSerializer
    methods = ['POST', 'PATCH', 'PUT', 'DELETE']

    def get_permissions(self):
        if self.request.method in self.methods:
            self.permission_classes = [IsAuthorOrAdmin]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(methods=['POST'], detail=True)
    def comment(self, request, pk=None):
        news = get_object_or_404(News, pk=pk)
        user = self.request.user
        text = request.data['text']
        comment = Comments.objects.create(
            author_id=user.id,
            news=news,
            text=text,
        )
        serializer = CommentSerializer(
            comment,
            context={'request': request},
        )
        return Response(serializer.data, HTTP_201_CREATED)
