from rest_framework import serializers, status


def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            raise serializers.ValidationError(f"{e}", code=status.HTTP_400_BAD_REQUEST)
    return wrapper
