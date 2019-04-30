"""
User Model 확장가능성을 염두하라.
1. django-admin startproject My_Project
2. accounts/models.py 에서 수정 시작
3. 아래 코드!
settings.py => INSTALLED APPS += 'accounts'
settings.py => AUTH.USERMODEL = 'accounts.User'
"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.


class User(AbstractUser):
    # username, password, first_name, last_name, email ...
    followings = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followers', blank=True)

    def __str__(self):
        return self.username
