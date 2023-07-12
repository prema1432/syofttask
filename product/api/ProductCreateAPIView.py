from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from product.permissions import AdminOnlyPermission
from product.serializers import ProductSerializer
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

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            return Response({'message': 'Product created successfully', 'product': serializer.data})
        return Response(serializer.errors, status=400)
