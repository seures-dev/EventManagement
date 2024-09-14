from django.contrib.auth import authenticate, login

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import EventSerializer, GuestSerializer, RegisterSerializer, UserSerializer
from .models import Event



class EventsView(APIView):

    @swagger_auto_schema(operation_description="Get all events", responses={200: EventSerializer(many=True)})
    def get(self, request: Request):
        return Response({'events': EventSerializer(Event.objects.all(), many=True).data})
    
    @swagger_auto_schema(
            operation_description="Create new Event", 
            request_body=EventSerializer, 
            responses={201: EventSerializer},
            )
    def post(self, request: Request):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)

        data = request.data.copy()
        serializer = EventSerializer(data=data)

        if serializer.is_valid():
            serializer.save(organizer=request.user)  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventView(APIView):

    @swagger_auto_schema(operation_description="Get event info by id", responses={200: EventSerializer, 404: 'Not found'})
    def get(self, request: Request, event_id: int):
        try:
            event = Event.objects.get(id=event_id)
            return Response( EventSerializer(event).data)
        except Event.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


    @swagger_auto_schema(operation_description="Delete event", responses={204: 'No Content', 403: 'Forbidden', 404: 'Not Found'})
    def delete(self, request: Request, event_id: int=None):
        try:
            self.permission_classes = [IsAuthenticated]
            self.check_permissions(request)
            event = Event.objects.get(id=event_id)
            if request.user != event.organizer:
                return Response({'detail': 'You do not have permission to delete this event.'}, status=status.HTTP_403_FORBIDDEN)
            event.delete()
        except Event.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    @swagger_auto_schema(operation_description="Update event", request_body=EventSerializer, responses={200: EventSerializer, 403: 'Forbidden', 404: 'Not Found'})
    def patch(self, request: Request, event_id: int=None):
        try:
            self.permission_classes = [IsAuthenticated]
            self.check_permissions(request)
            event = Event.objects.get(id=event_id)
            if request.user != event.organizer:
                return Response({'detail': 'You do not have permission to delete this event.'}, status=status.HTTP_403_FORBIDDEN)
        except Event.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EventSerializer(event, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RegistrationOnEvent(APIView):
    
    @swagger_auto_schema(operation_description="Register on event", request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'email': openapi.Schema(type=openapi.TYPE_STRING),
            'name': openapi.Schema(type=openapi.TYPE_STRING),
        }
    ), responses={201: GuestSerializer, 404: 'Event not found'})
    def post(self, request: Request, event_id):
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({'detail': 'Event not found.'}, status=status.HTTP_404_NOT_FOUND)
        data = request.data.copy()
        data['event'] = event.id
        guest = GuestSerializer(data=data)
        if guest.is_valid():
            guest.save()
            return Response(guest.data, status=status.HTTP_201_CREATED)
        return Response(guest.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
        
    @swagger_auto_schema(operation_description="Register new user", request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING),
            'email': openapi.Schema(type=openapi.TYPE_STRING),
            'password': openapi.Schema(type=openapi.TYPE_STRING),
            'password2': openapi.Schema(type=openapi.TYPE_STRING),
        }
    ), responses={201: 'User registered', 400: 'Bad Request'})
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'user': UserSerializer(user).data, 'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    
    @swagger_auto_schema(operation_description="Login user", request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING),
            'password': openapi.Schema(type=openapi.TYPE_STRING),
        }
    ), responses={200: 'User authenticated', 401: 'Invalid credentials'})
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'user': UserSerializer(user).data, 'token': token.key})
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    
