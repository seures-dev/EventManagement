from rest_framework import serializers
from .models import Event, Guest
from django.contrib.auth.models import User



    
class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.ReadOnlyField(source='organizer.username')  

    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'date', 'location', 'organizer')
        read_only_fields = ['id', 'organizer']


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('event', 'email', 'name')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password2')
        read_only_fields = ['id'] 

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords must match"})
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user