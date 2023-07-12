from django.contrib import admin

from product.models.product_models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ["created_by"]
    list_display = ("title", "price", "inventory_count", "is_active", "created_by")
    list_filter = ("is_active", "created_by")
    search_fields = ("title", "description")
    date_hierarchy = "created_at"
