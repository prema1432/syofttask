from django.urls import path

from product.api.ProductCreateAPIView import ProductCreateAPIView
from product.api.ProductDeleteAPIView import ProductDeleteAPIView
from product.api.ProductListAPIView import (PaginatedProductListAPIView,
                                            ProductListAPIView)
from product.api.ProductUpdateAPIView import ProductUpdateAPIView

urlpatterns = [
    path("create/", ProductCreateAPIView.as_view(), name="product-create"),
    path("list/", ProductListAPIView.as_view(), name="product-list"),
    # PaginatedProductListAPIView
    path(
        "list-paginated/",
        PaginatedProductListAPIView.as_view(),
        name="product-paginated-list",
    ),
    path("update/<uuid:pk>/", ProductUpdateAPIView.as_view(), name="product-update"),
    path("delete/<uuid:pk>/", ProductDeleteAPIView.as_view(), name="product-delete"),
]
