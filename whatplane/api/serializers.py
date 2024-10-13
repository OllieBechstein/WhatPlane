from rest_framework.serializers import ModelSerializer
from .models import Plane

class PlaneSerializer(ModelSerializer):
    class Meta:
        model = Plane
        fields = '__all__'