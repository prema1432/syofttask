from django.db import models


class RoleChoices(models.IntegerChoices):
    ADMIN = 1
    MANAGER = 2
    STAFF = 3
    CUSTOMER = 4
