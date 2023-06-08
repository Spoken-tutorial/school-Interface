from accounts.models import User
from common.serializers import LocationSerializer

from accounts.serializers.common_serializers import UserSerializer


def saveUser(user_data,obj=None):
    if obj:
        serializer = UserSerializer(obj,data=user_data,partial=True)
    else:
        serializer = UserSerializer(data=user_data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return user

def saveProfile(profile_data,user_id,obj=None):
    from accounts.serializers.user_serializers import ProfileSerializer
    if obj:
        serializer = ProfileSerializer(obj,data=profile_data,partial=True,context={'user_id': user_id})
    else:
        serializer = ProfileSerializer(data=profile_data,context={'user_id': user_id})
    serializer.is_valid(raise_exception=True)
    profile = serializer.save()
    return profile

def saveSchool(school_data,obj=None):
    from accounts.serializers.institution_serializers import SchoolSerializer
    if obj:
        serializer = SchoolSerializer(obj,data=school_data,partial=True)
    else:
        serializer = SchoolSerializer(data=school_data)
    serializer.is_valid(raise_exception=True)
    school = serializer.save()
    return school
    

def saveLocation(location_data,obj=None):
    """
    Saves a location with the provided data.

    Args:
        location_data (dict): The data for the location.
        obj (object, optional): An existing object to update. Defaults to None.
        partial (bool, optional): Specifies whether the update should be partial. Defaults to False.

    Returns:
        object: The saved location object.

    Raises:
        ValidationError: If the location data is invalid.
    """
    if obj:
        location_serializer = LocationSerializer(obj,data=location_data,partial=True)
    else:
        location_serializer = LocationSerializer(data=location_data)
    location_serializer.is_valid(raise_exception=True)
    return location_serializer.save()
    
    