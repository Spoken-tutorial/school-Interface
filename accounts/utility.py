from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation \
        import UserAttributeSimilarityValidator, CommonPasswordValidator
import string


def validate_user_password_constraints(password, dob=None):
    """
    Validate that the password meets the min & max length criteria. It has
    atleast 1 uppercase, lowercase, digit & punctuation character.
    Password should not be too similar to date of birth.

    If the password is valid, return ``None``.
    If the password is invalid, raise ValidationError for all error messages.
    """
    error_msg = ''
    cpv = CommonPasswordValidator()
    cpv.validate(password)
    if len(password) < 8:
        error_msg += "Password must be atleast 8 characters long. "
    if len(password) > 32:
        error_msg += "Password must be less than 32 characters. "
    if not any(char.isupper() for char in password):
        error_msg += "Password must contain at least one uppercase letter. "
    if not any(char.islower() for char in password):
        error_msg += "Password must contain at least one lowercase letter."
    if not any(char.isdigit() for char in password):
        error_msg += "Password must contain at least one digit."
    if not any(char in string.punctuation for char in password):
        error_msg += "Password must contain at least one punctuation character."
    if dob:
        dob1 = dob.strftime('%d%m%Y')
        dob2 = dob.strftime('%Y%m%d')
        if dob1 in password or dob2 in password:
            error_msg += "Password is too similar to the date of birth."
    if error_msg:
        raise ValidationError(f"{error_msg}")


class CustomPasswordValidator(UserAttributeSimilarityValidator):
    def validate(self, password, user=None, dob=None):
        super().validate(password, user)
        validate_user_password_constraints(password, dob)


class InputValue():
    def get(self):
        msg_recv = ["barath"]
        message = "Hello"
        msg_type = "single"
        rec_role = "parent"

        return msg_recv, rec_role, message, msg_type