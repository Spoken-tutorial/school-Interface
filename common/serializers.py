from rest_framework import serializers
from .models import State, District, City
from accounts.models import Location



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
        
class LocationSerializer(serializers.ModelSerializer):
     # Serializer fields for related models
    state = StateSerializer(read_only=True)
    district = DistrictSerializer(read_only=True)
    city = CitySerializer(read_only=True)
    # Integer fields for related model IDs
    state_id = serializers.IntegerField(write_only=True)
    district_id = serializers.IntegerField(write_only=True)
    city_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Location
        fields = ['address','state','district','city','pincode','state_id','district_id','city_id']
