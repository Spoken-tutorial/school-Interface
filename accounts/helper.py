from django.contrib.auth.hashers import make_password
from common.serializers import LocationSerializer


def set_encrypted_password(password):
    """
    Turn a plain-text password into a hash for database storage

    Args:
        password (str): The password to be encrypted.

    Returns:
        str: The encrypted password.
    """
    pwd = make_password(password)
    return pwd


def save_data(serializer, data, obj=None, context={}):
    """
    Saves data by creating a new object or updating an existing object.

    Args:
        serializer (Serializer): The serializer class to use.
        data (dict): A dictionary containing the data to be saved.
        obj (object, optional): An optional object representing an
        existing object. Defaults to None.
        context (dict, optional): An optional dictionary representing additional data
        for serializer. Defaults to None.

    Returns:
        object: The saved object.

    Raises:
        ValidationError: If the location data is invalid.
    """
    if obj:
        data_serializer = serializer(obj, data=data, partial=True)
    else:
        data_serializer = serializer(data=data, context=context)
    data_serializer.is_valid(raise_exception=True)
    return data_serializer.save()


def save_user_data(user_data, obj=None):
    """
    Saves user data by creating a new user or updating an existing user.

    Args:
        user_data (dict): A dictionary containing user data.
        obj (object, optional): An optional object representing an existing
        user. Defaults to None.

    Returns:
        object: The saved user object.

    Raises:
        ValidationError: If the user data is invalid.
    """
    from accounts.serializers.common_serializers import UserSerializer
    return save_data(UserSerializer, user_data, obj)


def save_profile_data(profile_data, user_id=None, obj=None):
    """
    Saves profile data by creating a new profile or updating an existing profile.

    Args:
        profile_data (dict): A dictionary containing profile data.
        user_id (int, optional): An optional user ID. Defaults to None.
        obj (object, optional): An optional object representing an existing
        profile. Defaults to None.

    Returns:
        object: The saved profile object.

    Raises:
        ValidationError: If the profile data is invalid.
    """
    from accounts.serializers.user_serializers import ProfileSerializer
    return save_data(ProfileSerializer, profile_data, obj, context={'user_id': user_id})


def save_location_data(location_data, obj=None):
    """
    Saves location data by creating a new location or updating an
    existing location.

    Args:
        location_data (dict): A dictionary containing profile data.
        obj (object, optional): An optional object representing an existing
        location. Defaults to None.

    Returns:
        object: The saved location object.

    Raises:
        ValidationError: If the location data is invalid.
    """
    return save_data(LocationSerializer, location_data, obj)
