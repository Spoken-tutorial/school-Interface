from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from accounts.models import TrainingTeam, CentralCoordinator, SchoolCoordinator, Teacher, \
        Parent
from accounts.serializers.institution_serializers import OrganisationSerializer, \
        SchoolSerializer
from accounts.serializers.common_serializers import ProfileSerializer
from accounts.helper import save_profile_data
from accounts.utility import CustomPasswordValidator
from accounts.decorators import handle_exceptions


COMMON_FIELDS_LIST = ['id', 'first_name', 'last_name', 'email',
                      'username', 'password', 'phone']


def clean_password(password, dob):
    CustomPasswordValidator().validate(password, dob=dob)
    return make_password(password)


class BaseUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)
    profile = ProfileSerializer()

    @handle_exceptions
    def create(self, validated_data, class_name=''):
        pwd = validated_data.get('password', '')
        dob = validated_data.get('profile').get('dob', '') if class_name != 'parent' else ''
        profile_data = validated_data.pop('profile', '')
        validated_data['password'] = clean_password(pwd, dob)
        instance = self.Meta.model.objects.create(**validated_data)
        if profile_data:
            profile = save_profile_data(profile_data, instance.user_ptr.id)
            instance.profile = profile
            instance.save()
        return instance

    @handle_exceptions
    def update(self, instance, validated_data):
        pwd = validated_data.get('password', '')
        if pwd:
            if type(instance).__name__ == 'Parent':
                validated_data['password'] = clean_password(pwd, '')
            else:
                dob = instance.profile.dob if (not validated_data.get('profile', '')) \
                    else validated_data.get('profile', '').get('dob', '')
                validated_data['password'] = clean_password(pwd, dob)
        profile_data = validated_data.pop('profile', None)
        if profile_data:
            save_profile_data(profile_data, None, instance.profile)
        if validated_data.items():
            super().update(instance, validated_data)
        return instance


class TrainingTeamSerializer(BaseUserSerializer):
    class Meta:
        model = TrainingTeam
        fields = COMMON_FIELDS_LIST + ['profile']

    def create(self, validated_data):
        return super().create(validated_data, class_name='training_team')


class CentralCoordinatorSerializer(BaseUserSerializer):
    organisation = OrganisationSerializer(read_only=True)
    organisation_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = CentralCoordinator
        fields = COMMON_FIELDS_LIST + ['profile', 'organisation', 'organisation_id']

    def create(self, validated_data):
        return super().create(validated_data, class_name='central_coordinator')


class SchoolCoordinatorSerializer(BaseUserSerializer):
    school = SchoolSerializer(read_only=True)
    school_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = SchoolCoordinator
        fields = COMMON_FIELDS_LIST + ['profile', 'school', 'school_id']

    def create(self, validated_data):
        return super().create(validated_data, class_name='school_coordinator')


class TeacherSerializer(BaseUserSerializer):
    school = SchoolSerializer(read_only=True)
    school_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Teacher
        fields = COMMON_FIELDS_LIST + ['profile', 'school', 'unique_id', 'school_id']

    def create(self, validated_data):
        return super().create(validated_data, class_name='teacher')


class ParentSerializer(BaseUserSerializer):

    class Meta:
        model = Parent
        fields = COMMON_FIELDS_LIST

    def create(self, validated_data):
        return super().create(validated_data, class_name='parent')
