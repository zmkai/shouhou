from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    account = models.CharField(max_length = 20)
    password= models.CharField(max_length = 6)
    telephone = models.CharField(max_length=11)

    class Meta:
        db_table = 'users_table'
