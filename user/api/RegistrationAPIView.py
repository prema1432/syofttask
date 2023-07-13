from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from user.config import RoleChoices
from user.serializers.UserSerializer import UserSerializer


class RegistrationAPIView(APIView):
    """
    Registration API View

    Endpoint: /api/register/

    Method: POST

    Request Body:
        - username (str): The username of the user.
        - email (str): The email address of the user.
        - password (str): The password of the user.
        - role (str): The role of the user (admin, manager, staff).

    Returns:
        - Success (201 Created): Returns a success message along with refresh and access tokens.
        - Error (400 Bad Request): Returns an error message if the request data is invalid.
    """

    @extend_schema(
        request=UserSerializer,
        responses={
            status.HTTP_201_CREATED: {"description": "User created successfully."}
        },
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            response_data = {
                "message": "User created successfully.",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "role": RoleChoices(user.role).name,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
