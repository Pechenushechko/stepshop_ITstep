from django.contrib.auth.models import AbstractUser
from django.db import models

class ShopUser(AbstractUser):
    avatar = models.ImageField(
        upload_to='users_avatars',
        blank=True,
        verbose_name="Avatar",
    )

    age = models.PositiveIntegerField(
        verbose_name='Age',

    )