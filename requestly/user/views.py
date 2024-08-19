# users/views.py

from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from .serializers import UserSerializer, TicketSerializer
from django.contrib.auth.models import User
from .models import UserDetail, ticket


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create (self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(
            {"message" :"User Created Successfully!", "data" : serializer.data},
            status = status.HTTP_201_CREATED,
            headers=headers 
        )

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Get the user's token and delete it
            request.user.auth_token.delete()
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"detail": "Invalid request."}, status=status.HTTP_400_BAD_REQUEST)
        

class UserListView(generics.ListAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Only authenticated users can access this view

class TicketViewSet(viewsets.ModelViewSet):
    queryset = ticket.objects.all()
    serializer_class = TicketSerializer


    
