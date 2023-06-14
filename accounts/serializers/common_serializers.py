from rest_framework import serializers
from common.serializers import LocationSerializer
from accounts.utility import CustomPasswordValidator
from accounts.models import User, Profile
from accounts.helper import save_location_data


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'username']

    def validate(self, attrs):
        pwd = attrs.get('password')
        user = User(**attrs)
        if pwd:
            CustomPasswordValidator().validate(pwd, user=user)
        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        pwd = validated_data.pop('password', '')
        if pwd:
            instance.set_password(pwd)
            instance.save()
        return super().update(instance, validated_data)


class ProfileSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Profile
        fields = ['dob', 'gender',  'location', 'updated', 'user_id']

    def create(self, validated_data):
        validated_data['user_id'] = self.context.get('user_id')
        validated_data['location_id'] = save_location_data(
            validated_data.pop('location')).id
        return super().create(validated_data)

    def update(self, instance, validated_data):
        location_data = validated_data.pop('location')
        if location_data:
            save_location_data(location_data, instance.location)
        return super().update(instance, validated_data)
