from rest_framework import serializers

from product.models.product_models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "inventory_count",
            "price",
            "is_active",
            "created_by",
            "updated_by",
            "created_at",
            "updated_at",
        ]


class ProductPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["title", "description", "inventory_count", "price"]


class ProductPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["title", "description", "inventory_count", "price"]
