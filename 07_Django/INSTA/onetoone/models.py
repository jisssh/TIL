from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.TextField(max_length=50, default='')

    def __str__(self):
        return f'{self.id}:{self.email}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    last_name = models.CharField(max_length=50, default='')
    first_name = models.CharField(max_length=50, default='')

    def __str(self):
        return f'{self.id}:{self.first_name}{self.last_name}'
