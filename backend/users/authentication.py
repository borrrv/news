from .models import Users
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = get_authorization_header(request).split()
        if not auth_header or auth_header[0].lower() != b"token":
            return None
        if len(auth_header) == 1:
            raise AuthenticationFailed("Токен не валидный")
        try:
            token = auth_header[1].decode("utf-8")
        except UnicodeError:
            raise AuthenticationFailed("Токен не валидный")
        token_obj = Token.objects.filter(key=token)
        if not token_obj:
            raise AuthenticationFailed("Токен не существует")
        return token_obj.first().user, None
