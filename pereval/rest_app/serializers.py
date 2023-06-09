from .models import *
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CoordinatesSerializer(ModelSerializer):
    class Meta:
        model = Coordinates
        fields = '__all__'


class PerevalSerializer(ModelSerializer):
    class Meta:
        model = Pereval
        fields = '__all__'


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'


class LevelSerializer(ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'