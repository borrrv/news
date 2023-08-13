from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response
from rest_framework.status import (HTTP_201_CREATED, HTTP_204_NO_CONTENT,
                                   HTTP_405_METHOD_NOT_ALLOWED)
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from news.models import Comments, News

from .permissions import IsAuthorOrAdmin
from .serializers import CommentSerializer, NewsSerializer


class GetAuthToken(TokenObtainPairView):
    authentication_classes = []


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all().select_related('author')
    serializer_class = NewsSerializer
    methods = ['POST', 'PUT', 'DELETE']

    def get_permissions(self):
        if self.request.method in self.methods:
            self.permission_classes = [IsAuthorOrAdmin]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(methods=['POST', 'GET'], detail=True)
    def comment(self, request, pk=None):
        news = get_object_or_404(News, pk=pk)
        if request.method == 'POST':
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
        if request.method == 'GET':
            comments = Comments.objects.filter(news=news)
            paginator = PageNumberPagination()
            result_page = paginator.paginate_queryset(comments, request)
            serializer = CommentSerializer(
                result_page,
                many=True,
                context={'request': request},
            )
            return paginator.get_paginated_response(serializer.data)

    @action(methods=['POST', 'DELETE'], detail=True)
    def like(self, request, pk=None):
        user = self.request.user
        news = get_object_or_404(News, pk=pk)
        if self.request.method == 'POST':
            news.likes.add(user)
            content = {"message": "Вы поставили лайк на новость"}
            return Response(content, status=HTTP_201_CREATED)
        if self.request.method == 'DELETE':
            news.likes.remove(user)
            content = {"message": "Вы убрали лайк с новости"}
            return Response(content, status=HTTP_204_NO_CONTENT)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comments.objects.all().select_related('author')

    def get_permissions(self):
        if self.request.method not in SAFE_METHODS:
            self.permission_classes = [IsAuthorOrAdmin]
        return super().get_permissions()

    def update(self, request, *args, **kwargs):
        return Response(status=HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request, *args, **kwargs):
        return Response(status=HTTP_405_METHOD_NOT_ALLOWED)
