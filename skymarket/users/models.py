from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from django.utils import timezone



from django.utils.translation import gettext_lazy as _

from users.managers import UserManager

NULLABLE = {'null': True, 'blank': True}


class UserRoles(models.TextChoices):
    # TODO закончите enum-класс для пользователя
    USER = 'user', _('user')
    ADMIN = 'admin', _('admin')


class User(AbstractBaseUser):
    # TODO переопределение пользователя.
    # TODO подробности также можно поискать в рекоммендациях к проекту

    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=30, verbose_name='телефон', **NULLABLE)
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.USER)
    last_login = models.DateTimeField(default=timezone.now, verbose_name='последняя авторизация')

    first_name = models.CharField(max_length=50, verbose_name='имя')
    last_name = models.CharField(max_length=50, verbose_name='фамилия', **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='активный')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
