from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from product.models.product_models import Product

from product.permissions import AdminOrManagerPermission
from product.serializers import ProductSerializer
class ProductListAPIView(APIView):
    """
    Product List View

    Endpoint: /api/product/list/

    Method: GET

    Required Permissions: Admin or Manager
    """

    permission_classes = [IsAuthenticated, AdminOrManagerPermission]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
