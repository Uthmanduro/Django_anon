from django.contrib.auth import logout
from .models import Message
from .serializers import MessageSerializer, UserSerializer
from rest_framework import generics, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_yasg.utils import swagger_auto_schema

class MessageAPI(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny(),]
        if self.request.method == 'GET':
            return [IsAuthenticated(),]
        
        
    def get(self, request, username=None):
        try:
            messages = Message.objects.filter(user=request.user.id)
        except User.DoesNotExist:
            return Response({'error': 'Not found'}, status.HTTP_404_NOT_FOUND)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    
    def post(self, request, username, *args, **kwargs):
        try:
            get_user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'error': 'Not found'}, status.HTTP_404_NOT_FOUND)
        print(get_user)
        new_data = {**request.data, 'user': get_user.id}

        serializer = self.get_serializer(data=new_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        message = serializer.data

        return Response(message, status.HTTP_201_CREATED)




class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        new_data = serializer.data
        new_data['profile_link'] = request.build_absolute_uri('/') + new_data['username']
        refresh = RefreshToken.for_user(user)
        
        new_data['access_token'] = str(refresh.access_token)
        new_data['refresh_token'] = str(refresh)
        return Response(new_data, status.HTTP_201_CREATED)


class LoginUser(generics.CreateAPIView):
    #queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        username = serializer.initial_data['username']
        password = serializer.initial_data['password']
        try: 
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            return Response({'error': 'username or password does not match'}, status.HTTP_401_UNAUTHORIZED)
        
        new_data = {}
        refresh = RefreshToken.for_user(user)

        new_data['access_token'] = str(refresh.access_token)
        new_data['refresh_token'] = str(refresh)
        return Response(new_data, status.HTTP_201_CREATED)
        # else:
        #     return Response({'error': 'username or password does not match'}, status.HTTP_401_UNAUTHORIZED)


class LogoutUser(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)


class UpdateUserDetails(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user