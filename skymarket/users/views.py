
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import User
from users.serializers import *


class UserListCreateAPIView(generics.ListCreateAPIView):
    """
    Класс возвращает всех пользователей при GET-запросе
    Класс создает нового пользователя при Post-запросе
    """
    serializer_class = UserDefaultSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    """
    Класс возвращает текущего пользователя при GET-запросе
    Класс редактирует текущего пользователя при Put/PATCH-запросе
    """
    serializer_class = UserDefaultSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserSetPasswordAPIView(generics.CreateAPIView):
    """
    Класс меняет текущий пароль на новый при POST-запросе
    """
    serializer_class = UserSetPasswordSerializer
    permission_classes = [IsAuthenticated]


class AnotherUserRetrieveAPIView(generics.RetrieveAPIView):
    """
    Класс показывает детали выбранного пользователя при GET-запросе
    """
    serializer_class = UserDefaultSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]