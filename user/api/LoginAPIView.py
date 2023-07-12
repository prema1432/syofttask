from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User


class LoginAPIView(APIView):
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
            }
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(
            {"message": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST
        )
