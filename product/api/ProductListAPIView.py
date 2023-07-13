from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models.product_models import Product
from product.permissions import AdminOrManagerPermission
from product.serializers.ProductSerializer import ProductSerializer
from rest_framework.pagination import PageNumberPagination


class ProductListAPIView(APIView):
    """
    Product List View

    Endpoint: /api/product/list/

    Method: GET

    Required Permissions: Admin or Manager
    """

    permission_classes = [IsAuthenticated, AdminOrManagerPermission]

    @extend_schema(
        description="Retrieve a list of products",
        responses={200: ProductSerializer(many=True)},
    )
    def get(self, request, format=None):
        """
        Retrieve a list of products.

        Returns:
            - Success (200 OK): Returns a list of serialized products.
        """
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductPagination(PageNumberPagination):
    page_size = 10



class PaginatedProductListAPIView(APIView):
    """
    Product List View

    Endpoint: /api/product/list/

    Method: GET

    Required Permissions: Admin or Manager
    """

    permission_classes = [IsAuthenticated, AdminOrManagerPermission]
    pagination_class = ProductPagination

    @extend_schema(
        description="Retrieve a list of products",
        responses={200: ProductSerializer(many=True)},
    )
    def get(self, request, format=None):
        """
        Retrieve a list of products.

        Returns:
            - Success (200 OK): Returns a list of serialized products.
        """
        products = Product.objects.all()
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
