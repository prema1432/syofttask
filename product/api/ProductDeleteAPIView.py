from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models.product_models import Product
from product.permissions import AdminOnlyPermission


class ProductDeleteAPIView(APIView):
    """
    Product Delete View

    Endpoint: /api/product/delete/<uuid:pk>/

    Method: DELETE

    Required Permissions: Admin Only
    """

    permission_classes = [IsAuthenticated, AdminOnlyPermission]

    @extend_schema(
        parameters=[
            {
                "name": "pk",
                "in": "path",
                "type": "string",
                "format": "uuid",
                "description": "The UUID of the product to be deleted.",
                "required": True,
            }
        ],
        responses={200: {"description": "Product deleted successfully"}},
    )
    def delete(self, request, pk):
        """
        Delete a product.

        Parameters:
            - pk (str): The UUID of the product.

        Returns:
            - Success (200 OK): Returns a success message if the product is deleted successfully.
            - Error (404 Not Found): Returns an error message if the product with the given UUID is not found.
        """
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"message": "Product not found"}, status=404)

        product.delete()
        return Response({"message": "Product deleted successfully"})
