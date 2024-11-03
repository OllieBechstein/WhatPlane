from rest_framework.serializers import ModelSerializer
from .models import Plane, UserProfile

class PlaneSerializer(ModelSerializer):
    class Meta:
        model = Plane
        fields = '__all__'

class UserProfileSerializer(ModelSerializer):
    username = ModelSerializer.CharField(source='user.username', read_only=True)
    class Meta:
        model = UserProfile
        fields = ['username', 'score']