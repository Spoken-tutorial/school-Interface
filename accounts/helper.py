from django.contrib.auth.hashers import make_password
from common.serializers import LocationSerializer
from .models import GroupPermission


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


def manage_group_permissions(group, permissions):
    """
    Manages group permissions for a given group by processing a dictionary of permissions.

    Args:
        group (Group): The group for which permissions are managed.
        permissions (dict): A dictionary containing permission data.

    The `permissions` dictionary should have the following structure:
    {
        "permission_id_1": {
            "status": True or False,  # Indicates whether the permission
            is granted or revoked.
            "context": context_id or None  # context associated with the permission.
        },
        # Additional permission entries...
    }

    For each permission in the dictionary, this function either grants or revokes
    the permission for the group.
    If "status" is True, the permission is granted. If "status" is False,
    the permission is revoked.
    The "context" field can specify additional context for the permission.

    Returns:
        None

    This function performs the necessary operations on the `GroupPermission` model
    based on the provided data.
    It creates new permissions or deletes existing ones according to the specified status.
    Any exceptions that occur during this process are printed to the console
    for debugging purposes.
    """
    for permission, permission_data in permissions.items():
        permission_id = int(permission)
        context_id = permission_data.get('context', None)
        status = permission_data.get('status', False)
        try:
            if status:
                gp = GroupPermission.objects.filter(role=group, permission_id=permission_id
                                                    ).first()
                if gp:
                    gp.context_id = context_id
                    gp.save()
                else:
                    GroupPermission.objects.create(role=group,
                                                   permission_id=permission_id,
                                                   context_id=context_id)
            else:
                gp = GroupPermission.objects.get(role=group,
                                                 permission_id=permission_id,
                                                 context_id=context_id)
                gp.delete()
        except Exception as e:
            print(f"\033[93mException **  {e}\033[0m")
