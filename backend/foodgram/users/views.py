from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin,
)
from rest_framework.response import Response
from rest_framework import status

from . models import Subscribe, User
from . serializers import (
    UserSerializer,
    UserChangePasswordSerializer,
    GetTokenSerializer,
    # CustomTokenObtainPairSerializer,
)


class UserViewSet(
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, GenericViewSet,
):
    """
    Вьюсет для работы с пользователями.
    URL - /users/.
    """

    name = 'Обработка запросов о пользователях'
    description = 'Обработка запросов о пользователях'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action == 'set_password':
            return UserChangePasswordSerializer
        return UserSerializer


    @action(
        methods =['POST',],
        url_path = 'set_password',
        detail = False
    )
    def set_password(self, request):
        """
        Метод для обработки запроса POST на изменение пароля авторизованным
        пользователем.
        URL - /users/set_password.
        """
        user = request.user
        serializer = self.get_serializer(user, data=request.data)
        if serializer.is_valid():
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(
        methods =['GET',],
        url_path = 'me',
        detail = False
    )
    def me(self, request):
        """
        Метод для обработки запроса GET на получение данных профиля текущего
        пользователя.
        URL - /users/me.
        """
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data, status = status.HTTP_200_OK)


class GetTokenView(APIView):
    """
    Класс для обработки POST запросов для получения токена авторизации по email
    и паролю.
    URL - /auth/token/login/.
    """

    def post(self, request):
        serializer = GetTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(email=serializer.validated_data['email'])
            # token = RefreshToken.for_user(user)
            return Response(
                {'auth_token': ''},#str(token.access_token)},
                status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DelTokenView(APIView):
    """
    Класс для обработки POST запросов для удаления токена авторизации текущего
    пользователя.
    URL - /auth/token/logout/.
    """

    # authentication_classes = []


    def post(self, request):
        token = request.auth
        
        return Response(status=status.HTTP_204_NO_CONTENT)
