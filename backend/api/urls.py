from django.urls import path
from .views import GetAuthToken
#from users.authentication


urlpatterns = [
    path("auth/", GetAuthToken.as_view()),
]
