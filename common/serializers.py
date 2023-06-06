from rest_framework import serializers
from .models import State, District, City


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['name']


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['name']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name']
