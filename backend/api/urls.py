from django.urls import path, include
from .views import GetAuthToken
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet


router = DefaultRouter()

router.register("news", NewsViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("auth/", GetAuthToken.as_view()),
]
