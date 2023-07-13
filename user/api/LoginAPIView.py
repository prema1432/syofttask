from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from user.config import RoleChoices
from user.models import User
from user.serializers.UserSerializer import UserLoginSerializer, UserSerializer


class LoginAPIView(APIView):
    """
    Login API View

    Endpoint: /api/login/

    Method: POST

    Request Body:
        - email (str): The email address of the user.
        - password (str): The password of the user.

    Returns:
        - Success (200 OK): Returns a success message along with refresh and access tokens.
        - Error (400 Bad Request): Returns an error message if the credentials are invalid.
    """

    @extend_schema(
        request=UserLoginSerializer,
        responses={status.HTTP_200_OK: {"description": "Login successful."}},
    )
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {"message": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST
            )

        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            response_data = {
                "message": "Login successful.",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "role": RoleChoices(user.role).name,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(
            {"message": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST
        )
