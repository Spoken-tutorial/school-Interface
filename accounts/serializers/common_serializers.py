from rest_framework import serializers
from accounts.utility import CustomPasswordValidator
from accounts.models import User,Profile
from common.serializers import LocationSerializer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password','username']
    
    def validate(self, attrs):
        pwd = attrs.get('password')
        user = User(**attrs)
        if pwd:
            pwd_validator = CustomPasswordValidator()
            pwd_validator.validate(pwd,user=user)
        return super().validate(attrs)
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    def update(self, instance, validated_data):
        pwd = validated_data.pop('password','')
        if pwd:
            instance.set_password(pwd)
            instance.save()
        return super().update(instance, validated_data)
    
    
class ProfileSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Profile  
        fields = ['dob','gender','phone','location','updated','user_id']
    
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
            locationSerializer = LocationSerializer(instance.location,location,partial=True)
            locationSerializer.is_valid(raise_exception=True)
            locationSerializer.save()
        instance.dob = validated_data.get('dob', instance.dob)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        instance = super().update(instance,validated_data)
        return instance