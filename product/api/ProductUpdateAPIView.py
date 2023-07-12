from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from product.models.product_models import Product

from product.permissions import AdminOrManagerPermission
from product.serializers import ProductSerializer

class ProductUpdateAPIView(APIView):
    """
    Product Update View

    Endpoint: /api/product/update/<int:pk>/

    Method: PUT

    Request Body:
        - title (str): The updated title of the product.
        - description (str): The updated description of the product.
        - inventory_count (int): The updated inventory count of the product.
        - price (float): The updated price of the product.

    Required Permissions: Admin or Manager
    """

    permission_classes = [IsAuthenticated, AdminOrManagerPermission]

    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'message': 'Product not found'}, status=404)

        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            return Response({'message': 'Product updated successfully', 'product': serializer.data})
        return Response(serializer.errors, status=400)
