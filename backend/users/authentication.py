import os
from datetime import datetime

import jwt
from dotenv import load_dotenv
from rest_framework.authentication import (BaseAuthentication,
                                           get_authorization_header)
from rest_framework.exceptions import AuthenticationFailed

from config.settings import ALGORITHMS, BASE_DIR

from .models import Users

load_dotenv(BASE_DIR)


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = get_authorization_header(request).split()
        if not auth_header or auth_header[0].lower() != b"bearer":
            return None
        if len(auth_header) == 1:
            raise AuthenticationFailed("Токен не валидный")
        try:
            token = auth_header[1].decode("utf-8")
        except UnicodeError:
            raise AuthenticationFailed("Токен не валидный")
        return self.authenticate_credential(token)

    def authenticate_credential(self, token):
        try:
            payload = jwt.decode(
                token, os.getenv("SECRET_KEY"), algorithms=ALGORITHMS
            )
        except jwt.PyJWTError:
            raise AuthenticationFailed("Не получилось декодировать токен")
        token_exp = datetime.fromtimestamp(payload["exp"])
        if token_exp < datetime.utcnow():
            raise AuthenticationFailed("Время токена истекло")
        try:
            user = Users.objects.get(id=payload["user_id"])
        except Users.DoesNotExist:
            raise AuthenticationFailed(
                "Пользователь с таким токеном не найден"
            )
        return user, None
