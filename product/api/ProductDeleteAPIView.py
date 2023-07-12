from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from product.models.product_models import Product

from product.permissions import AdminOnlyPermission
class ProductDeleteAPIView(APIView):
    """
    Product Delete View

    Endpoint: /api/product/delete/<int:pk>/

    Method: DELETE

    Required Permissions: Admin Only
    """

    permission_classes = [IsAuthenticated, AdminOnlyPermission]

    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'message': 'Product not found'}, status=404)

        product.delete()
        return Response({'message': 'Product deleted successfully'})