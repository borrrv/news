from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GetAuthToken, NewsViewSet

router = DefaultRouter()

router.register("news", NewsViewSet)
router.register("comment", CommentViewSet, basename="comment")

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", GetAuthToken.as_view()),
]
