from rest_framework import serializers
from accounts.models import TrainingTeam, CentralCoordinator, SchoolCoordinator, Teacher, Parent, Student
from accounts.serializers.institution_serializers import OrganisationSerializer, SchoolSerializer
from accounts.serializers.common_serializers import UserSerializer,ProfileSerializer
from accounts.helper import saveUser, saveProfile, saveSchool


class TrainingTeamSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    profile = ProfileSerializer()
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = TrainingTeam
        fields = ['id','user','profile']
    
    def create(self,validated_data):
        user = saveUser(validated_data.pop('user')) # save the nested user instance
        profile = saveProfile(validated_data.pop('profile'),user.id) # save the nested profile instance
        instance = TrainingTeam.objects.create(**validated_data, user=user, profile=profile)
        return instance
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user',None)
        profile_data = validated_data.pop('profile',None)
        if user_data:
            saveUser(user_data, instance.user)
        if profile_data:
            saveProfile(profile_data,instance.user.id,instance.profile)
        return instance
    

class CoordinatorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer()
    profile = ProfileSerializer()

    def create_coordinator_profile(self, validated_data):
        user = saveUser(validated_data.pop('user')) # save the nested user instance
        profile = saveProfile(validated_data.pop('profile'),user.id) # save the nested profile instance
        return user, profile
    
    def update_coordinator_profile(self, instance, data):
        user_data = data.pop('user','')
        if user_data:
            saveUser(user_data,instance.user)
        profile_data = data.pop('profile','')
        if profile_data:
            saveProfile(profile_data,instance.user.id,instance.profile)
        return data
    
class CentralCoordinatorSerializer(CoordinatorSerializer):
    organisation = OrganisationSerializer(read_only=True)
    organisation_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = CentralCoordinator
        fields = ['id','user','profile','organisation','organisation_id']    
        
    def create(self, validated_data):
        user, profile = super().create_coordinator_profile(validated_data)
        return CentralCoordinator.objects.create(**validated_data,user=user,profile=profile)
    
    def update(self, instance, validated_data):
        validated_data = super().update_coordinator_profile(instance, validated_data)
        return super().update(instance, validated_data)
    
class SchoolCoordinatorSerializer(CoordinatorSerializer):
    school = SchoolSerializer(read_only=True)
    school_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = SchoolCoordinator
        fields = ['id','user','profile','school','school_id']
        
    def create(self, validated_data):
        user, profile = super().create_coordinator_profile(validated_data)
        return SchoolCoordinator.objects.create(**validated_data,user=user,profile=profile)
    
    def update(self, instance, validated_data):
        validated_data = super().update_coordinator_profile(instance, validated_data)
        return super().update(instance, validated_data)
    
    
class TeacherSerializer(SchoolCoordinatorSerializer):
    
    class Meta:
        model = Teacher
        fields = ['id','user','profile','school','unique_id','school_id']
    
    def create(self, validated_data):
        user, profile = super().create_coordinator_profile(validated_data)
        return Teacher.objects.create(**validated_data,user=user,profile=profile)
    
    def update(self, instance, validated_data):
        validated_data = super().update_coordinator_profile(instance, validated_data)
        unique_id = validated_data.pop('unique_id','')
        if unique_id:
            instance.unique_id = unique_id
        instance.save() 
        return instance
    
class ParentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Parent
        fields = ['id','user']
        
        
