from rest_framework import serializers
from .models import User, Profile, TrainingTeam, Location
from common.serializers import StateSerializer, DistrictSerializer, CitySerializer
from .utility import CustomPasswordValidator


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
        fields = ['address', 'state', 'district', 'city', 'pincode', 'state_id',
                  'district_id', 'city_id']


class ProfileSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Profile
        fields = ['dob', 'gender', 'phone', 'location', 'updated', 'user_id']

    def create(self, validated_data):
        user_id = self.context.get('user_id')
        validated_data['user_id'] = user_id
        location = validated_data.pop('location')
        locationSerializer = LocationSerializer(data=location)
        locationSerializer.is_valid()
        location_obj = locationSerializer.save()
        validated_data['location_id'] = location_obj.id
        instance = super().create(validated_data)
        return instance

    def update(self, instance, validated_data):
        location = validated_data.pop('location')
        if location:
            locationSerializer = LocationSerializer(instance.location, location,
                                                    partial=True)
            locationSerializer.is_valid(raise_exception=True)
            locationSerializer.save()
        instance.dob = validated_data.get('dob', instance.dob)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        instance = super().update(instance, validated_data)
        return instance


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'username']

    def validate(self, attrs):
        pwd = attrs.get('password')
        user = User(**attrs)
        if pwd:
            pwd_validator = CustomPasswordValidator()
            pwd_validator.validate(pwd, user=user)
        return super().validate(attrs)


class TrainingTeamSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    profile = ProfileSerializer()

    class Meta:
        model = TrainingTeam
        fields = ['user', 'profile']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        profile_data = validated_data.pop('profile')
        user = UserSerializer(data=user_data)
        user.is_valid(raise_exception=True)
        user_obj = user.save()
        profile = ProfileSerializer(data=profile_data,
                                    context={'user_id': user_obj.id})
        profile.is_valid(raise_exception=True)
        profile_obj = profile.save()
        validated_data['user'] = user_obj
        validated_data['profile'] = profile_obj
        instance = super().create(validated_data)
        return instance

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        profile_data = validated_data.pop('profile', None)

        if user_data:
            user_data.pop('password', None)
            user_serializer = UserSerializer(instance.user, data=user_data,
                                             partial=True)
            user_serializer.is_valid(raise_exception=True)
            user = user_serializer.save()
        else:
            user = instance.user

        if profile_data:
            profile_serializer = ProfileSerializer(instance.profile,
                                                   data=profile_data,
                                                   partial=True)
            profile_serializer.is_valid(raise_exception=True)
            profile = profile_serializer.save()
        else:
            profile = instance.profile
        instance.user = user
        instance.profile = profile
        instance.save()
        return instance
