from rest_framework import serializers
from accounts.models import Organisation, School
from accounts.serializers.common_serializers import UserSerializer
from accounts.helper import save_user_data, save_location_data
from common.serializers import LocationSerializer

COMMON_FIELDS = ['id', 'name_of_association', 'date_of_association',
                 'type', 'updated', 'location', 'added_by', 'is_active']


class BaseAssociationSerializer(serializers.ModelSerializer):
    """
    Base serializer for common functionality.
    """
    id = serializers.IntegerField(read_only=True)
    added_by = UserSerializer()
    updated = serializers.DateField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    location = LocationSerializer()

    def save_nested_data(self, validated_data, instance, nested_field, serializer_class):
        """
        Save nested data for a given field using the provided serializer class.

        Args:
            validated_data (dict): The validated data containing the nested field.
            instance (object): The instance of the model.
            nested_field (str): The name of the nested field.
            serializer_class (Serializer): The serializer class to use.
        """
        nested_data = validated_data.pop(nested_field, '')
        if nested_data:
            serializer = serializer_class(instance=getattr(instance, nested_field),
                                          data=nested_data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

    def create(self, validated_data):
        user = save_user_data(validated_data.pop('added_by'))
        location = save_location_data(validated_data.pop('location'))
        instance = self.Meta.model.objects.create(**validated_data,
                                                  added_by=user, location=location)
        return instance

    def update(self, instance, validated_data):
        self.save_nested_data(validated_data, instance, 'added_by', UserSerializer)
        self.save_nested_data(validated_data, instance, 'location', LocationSerializer)
        return super().update(instance, validated_data)


class OrganisationSerializer(BaseAssociationSerializer):
    class Meta:
        model = Organisation
        fields = COMMON_FIELDS


class SchoolSerializer(BaseAssociationSerializer):
    organisation = OrganisationSerializer(read_only=True)
    organisation_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = School
        fields = COMMON_FIELDS + ['organisation', 'organisation_id']
