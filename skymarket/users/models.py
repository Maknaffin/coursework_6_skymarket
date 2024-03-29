from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

NULLABLE = {"null": True, "blank": True}


class UserRoles(models.TextChoices):
    ADMIN = "Admin"
    USER = "User"


class User(AbstractBaseUser):
    username = None
    first_name = models.CharField(max_length=50, verbose_name='Имя пользователя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия пользователя')
    phone = models.CharField(max_length=15, verbose_name='Телефон пользователя')
    email = models.EmailField(unique=True, verbose_name='Почта пользователя')
    role = models.CharField(max_length=10, default=UserRoles.USER, choices=UserRoles.choices, verbose_name="Роль пользователя")
    image = models.ImageField(upload_to='profile_images', verbose_name='Аватарка пользователя', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='Активность пользователя')

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER
