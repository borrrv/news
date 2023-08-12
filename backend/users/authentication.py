from .models import Users
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            return None
        try:
            user = Users.objects.get(username=username)
        except Users.DoesNotExist:
            raise AuthenticationFailed('Такого пользователя не существует')
        else:
            if not user.check_password(password):
                raise AuthenticationFailed('Неверный пароль')
        return (user, None)
