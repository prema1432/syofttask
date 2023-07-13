from django.db import models

from .base_models import BaseModel


class Product(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    inventory_count = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        "user.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="products_created",
    )
    updated_by = models.ForeignKey(
        "user.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="products_updated",
    )

    def __str__(self):
        return self.title
