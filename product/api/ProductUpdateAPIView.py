from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models.product_models import Product
from product.permissions import AdminOrManagerPermission
from product.serializers.ProductSerializer import (ProductPatchSerializer,
                                                   ProductPostSerializer,
                                                   ProductSerializer)


class ProductUpdateAPIView(APIView):
    """
    Product Update View

    Endpoint: /api/product/update/{pk}/

    Method: PUT

    Request Body:
        - title (str): The updated title of the product.
        - description (str): The updated description of the product.
        - inventory_count (int): The updated inventory count of the product.
        - price (float): The updated price of the product.

    Required Permissions: Admin or Manager
    """

    permission_classes = [IsAuthenticated, AdminOrManagerPermission]

    @extend_schema(
        request=ProductPatchSerializer,
        responses={200: ProductPatchSerializer(many=False)},
    )
    def put(self, request, pk):
        """
        Update an existing product.

        Parameters:
            - pk (uuid): The UUID identifier of the product.

        Returns:
            - Success (200 OK): Returns a success message along with the updated product.
            - Error (404 Not Found): Returns an error message if the product is not found.
            - Error (400 Bad Request): Returns an error message if the request data is invalid.
        """
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductPatchSerializer(product, data=request.data)
        if serializer.is_valid():
            product = serializer.save(updated_by=self.request.user)
            return Response(
                {"message": "Product updated successfully", "product": serializer.data}
            )
        return Response(serializer.errors, status=400)
