import uuid
from django.contrib.auth import authenticate, get_user_model
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from .serializers import RegisterSerializer, LoginSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)
        if not user:
            return Response(
                {"error": "Invalid username or password"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        })
    

class GuestLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = f"guest_{uuid.uuid4().hex[:8]}"
        random_password = uuid.uuid4().hex

        user = User.objects.create_user(
            username=username,
            password=random_password
        )
        user.is_guest = True
        user.save()

        refresh = RefreshToken.for_user(user)

        return Response({
            "guest": True,
            "username": username,
            "access": str(refresh.access_token)
        })
