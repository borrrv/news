from rest_framework_simplejwt.views import TokenObtainPairView
from users.authentication import CustomAuthentication


class GetAuthToken(TokenObtainPairView):
    authentication_classes = [CustomAuthentication]
