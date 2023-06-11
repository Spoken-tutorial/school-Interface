from rest_framework import serializers
from accounts.models import Organisation, School, User
from accounts.serializers.common_serializers import UserSerializer
from accounts.helper import saveUser, saveLocation
from common.serializers import LocationSerializer


class OrganisationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Organisation model.
    """
    id = serializers.IntegerField(read_only=True)
    added_by = UserSerializer()
    date_of_association = serializers.DateField()
    updated = serializers.DateField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    location = LocationSerializer()

    class Meta:
        model = Organisation
        fields = ['id', 'name_of_association', 'date_of_association', 'type', 'updated',
                  'location', 'added_by', 'is_active']

    def create(self, validated_data):
        user = saveUser(validated_data.pop('added_by'))  # save the nested user instance
        location = saveLocation(validated_data.pop('location'))
        organisation = Organisation.objects.create(**validated_data, added_by=user,
                                                   location=location)
        return organisation

    def update(self, instance, validated_data):
        # save the nested user instance
        user_data = validated_data.pop('added_by', '')
        if user_data:
            saveUser(user_data, user_obj=instance.added_by)

        # save the nested location instance
        location_data = validated_data.pop('location', '')
        if location_data:
            saveLocation(location_data, obj=instance.location)
        return super().update(instance, validated_data)


class SchoolSerializer(serializers.ModelSerializer):
    organisation = OrganisationSerializer(read_only=True)
    organisation_id = serializers.IntegerField(write_only=True)
    updated = serializers.BooleanField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    added_by = UserSerializer()
    location = LocationSerializer()

    class Meta:
        model = School
        fields = ['id', 'name_of_association', 'date_of_association', 'type',
                  'organisation', 'organisation_id', 'updated', 'is_active', 'added_by',
                  'location']

    def create(self, validated_data):
        user = saveUser(validated_data.pop('added_by'))  # save the nested user instance
        location = saveLocation(validated_data.pop('location'))
        school = School.objects.create(**validated_data, added_by=user, location=location)
        return school

    def update(self, instance, validated_data):
        # save the nested user instance
        user_data = validated_data.pop('added_by', '')
        if user_data:
            saveUser(user_data, instance.added_by)
        # save the nested location instance
        location_data = validated_data.pop('location', '')
        if location_data:
            saveLocation(location_data, obj=instance.location)
        return super().update(instance, validated_data)

    def validate_added_by(self, value):
        if User.objects.filter(email=value.get('email')).exists():
            return value
        return value
