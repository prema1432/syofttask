from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from product.permissions import AdminOnlyPermission
from product.serializers.ProductSerializer import (ProductPostSerializer,
                                                   ProductSerializer)


class ProductCreateAPIView(APIView):
    """
    Product Create View

    Endpoint: /api/product/create/

    Method: POST

    Request Body:
        - title (str): The title of the product.
        - description (str): The description of the product.
        - inventory_count (int): The inventory count of the product.
        - price (float): The price of the product.

    Required Permissions: Admin Only
    """

    permission_classes = [IsAuthenticated, AdminOnlyPermission]

    @extend_schema(
        request=ProductPostSerializer,
        responses={200: ProductSerializer},
    )
    def post(self, request):
        """
        Create a new product.

        Parameters:
            - title (str): The title of the product.
            - description (str): The description of the product.
            - inventory_count (int): The inventory count of the product.
            - price (float): The price of the product.

        Returns:
            - Success (200 OK): Returns a success message along with the created product.
            - Error (400 Bad Request): Returns an error message if the request data is invalid.
        """
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save(created_by=self.request.user)
            return Response(
                {"message": "Product created successfully", "product": serializer.data}
            )
        return Response(serializer.errors, status=400)
