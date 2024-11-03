from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Plane, UserProfile

class PlaneSerializer(ModelSerializer):
    class Meta:
        model = Plane
        fields = '__all__'

class UserProfileSerializer(ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = UserProfile
        fields = ['username', 'score']