from django.contrib.auth.models import AbstractUser
from django.db import models

from user.config import RoleChoices


class User(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.IntegerField(
        default=RoleChoices.CUSTOMER.value, choices=RoleChoices.choices
    )
