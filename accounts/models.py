from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import Group

from common.models import State, District, City, Language

# Constants
APPROVAL_STATUS = [
        ('pending_approval', 'pending approval'),
        ('active', 'active'),
        ('inactive', 'inactive'),
        ('rejected', 'rejected')
    ]

class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    This custom user model retains the core functionality of Django's built-in user model
    while adding specific constraints:
    - Email is unique, ensuring each user has a distinct email address.
    - First name and last name are required fields, ensuring non-null values.
    """
    mobile_regex = RegexValidator(regex=r'[1-9][0-9]{10}$',
                                 message='Enter a valid mobile number')

    email = models.EmailField(unique=True, null=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=False,
                                  null=False)
    last_name = models.CharField(_("last name"), max_length=150, blank=False,
                                 null=False)
    phone = models.CharField(max_length=20, null=True, validators=[mobile_regex])

class Permission(models.Model):
    """
    The permissions system provides a way to assign permissions to groups.
    """
    name = models.CharField(_("name"), max_length=255)
    codename = models.CharField(_("codename"), max_length=100)

class Group(models.Model):
    """
    Groups are a generic way of categorizing users to apply permissions, or
    some other label, to those users. A user can belong to any number of
    groups. A user in a group automatically has all the permissions granted to that
    group.
    """
    name = models.CharField(_("name"), max_length=150, unique=True)
    added_by = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class GroupPermissions(models.Model):
    """
    Model representing permissions associated with a group.
    """
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    permission = models.ForeignKey(Permission, on_delete=models.PROTECT)
    added_by = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Location(models.Model):
    """
        Complete address for users
    """
    pincode_regex = RegexValidator(regex=r'^\d{6}$',
                                   message='Enter a valid pincode')

    address = models.TextField()
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    district = models.ForeignKey(District, on_delete=models.PROTECT)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    pincode = models.CharField(max_length=6, validators=[pincode_regex])
    updated = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return (f"{self.address}, {self.city}, {self.district}, {self.state} - "
                f"{self.pincode}")


class Profile(models.Model):
    """
        Profile information for users
    """
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')] 

    user = models.ForeignKey(User, on_delete=models.PROTECT,
                             related_name='profile_info')
    dob = models.DateField(help_text='YYYY-MM-DD')
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    updated = models.DateField(auto_now=True)

"""
Static roles section: Following models define the static roles.
"""

class OrganisationType(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Organisation(models.Model):
    added_by = models.ForeignKey(User, on_delete=models.PROTECT,
                                 related_name='associated_organisation')
    name_of_association = models.CharField(max_length=200, unique=True)
    date_of_association = models.DateField()
    type = models.ForeignKey(OrganisationType, on_delete=models.PROTECT)
    organisation = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    status = models.CharField(choices=APPROVAL_STATUS, max_length=100, default="pending_approval")
    approved_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    class Meta:
        ordering = ['name_of_association', '-date_of_association']

    def __str__(self):
        return self.name_of_association

class SchoolType(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class School(models.Model):
    added_by = models.ForeignKey(User, on_delete=models.PROTECT,
                                 related_name='school_added')
    name_of_association = models.CharField(max_length=200, unique=True)
    date_of_association = models.DateField()
    type = models.ForeignKey(SchoolType, on_delete=models.PROTECT)
    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT,
                                     null=True, blank=True)
    
    is_active = models.BooleanField(default=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    status = models.CharField(choices=APPROVAL_STATUS, max_length=100, default="pending_approval")
    approved_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    

    class Meta:
        ordering = ['name_of_association', '-date_of_association']

    def __str__(self):
        return self.name_of_association


class OrganisationAuthority(models.Model):
    """
    The 'organization authority' is the highest role within an organization's hierarchy of roles.
    Users holding this role has access to all activities and resources within the organization.
    """
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False, related_name="org_auth")
    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT)
    approved_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    status = models.CharField(choices=APPROVAL_STATUS, max_length=100, default="pending_approval")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Organisation Authority'
        verbose_name_plural = 'Organisation Authority'

    def __str__(self):
        return f"{self.user} - {self.organisation}"

class OrganisationCoordinator(models.Model):
    """
    An organisation coordinator is a user assigned to coordinate activities within a specific organisation.
    Each coordinator is associated with a user account and an organisation.
    """
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False, related_name="org_coordinator")
    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT)
    approved_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    status = models.CharField(choices=APPROVAL_STATUS, max_length=100, default="pending_approval")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Organisation Coordinator'
        verbose_name_plural = 'Organisation Coordinators'

    def __str__(self):
        return f"{self.user} - {self.organisation}"

class SchoolAuthority(models.Model):
    """
    The 'school authority' is the highest role within a school's hierarchy of roles.
    Users holding this role has access to all activities and resources within the school.
    """
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False, related_name="school_auth")
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    status = models.CharField(choices=APPROVAL_STATUS, max_length=100, default="pending_approval")
    approved_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'School Coordinator'
        verbose_name_plural = 'School Coordinators'

    def __str__(self):
        return f"{self.user} - {self.school}"


class SchoolCoordinator(models.Model):
    """
    An school coordinator is a user assigned to coordinate activities within a specific school.
    Each coordinator is associated with a user account and a school.
    """
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False, related_name="school_coordinator")
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    status = models.CharField(choices=APPROVAL_STATUS, max_length=100, default="pending_approval")
    approved_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'School Coordinator'
        verbose_name_plural = 'School Coordinators'

    def __str__(self):
        return f"{self.user} - {self.school}"



class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False, related_name="teacher_user")
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    unique_id = models.CharField(max_length=50)
    status = models.CharField(choices=APPROVAL_STATUS, max_length=100, default="pending_approval")
    approved_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name="approved_teachers")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"


class Parent(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False, related_name="user_parent")
    status = models.CharField(choices=APPROVAL_STATUS, max_length=100, default="pending_approval")
    approved_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name="approved_parent")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}"

class ClassName(models.Model):
    name = models.IntegerField()

class Section(models.Model):
    name = models.CharField(max_length=50)

class ClassCoordinator(models.Model):
    """
    An class coordinator is a user assigned to coordinate activities within a specific class & section.
    Each coordinator is associated with a user account, school, class & section.
    """
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="class_coordinator")
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    class_value = models.ForeignKey(ClassName, on_delete=models.PROTECT)
    section = models.ForeignKey(Section, on_delete=models.PROTECT)
    status = models.CharField(choices=APPROVAL_STATUS, max_length=100)
    approved_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    unique_id = models.CharField(max_length=100)  # Enrolment ID / Any other unique ID
    preferred_lang = models.ForeignKey(Language, on_delete=models.PROTECT)
    current_class = models.ForeignKey(ClassName, on_delete=models.PROTECT)
    division = models.ForeignKey(Section, on_delete=models.PROTECT)
    parent = models.ForeignKey(Parent, on_delete=models.PROTECT, related_name='children', null=True, blank=True)

    def __str__(self):
        return f"{self.username} - {self.school.name_of_association}"

class ClassTeacher(models.Model):
    """
    This model provides mapping of a teacher for a school, class & section.
    """
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, related_name="class_teacher")
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    class_value = models.ForeignKey(ClassName, on_delete=models.PROTECT)
    section = models.ForeignKey(Section, on_delete=models.PROTECT)
    status = models.CharField(choices=APPROVAL_STATUS, max_length=100, default="pending_approval")
    approved_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

"""
Static roles section ends.
"""


"""
Dynamic roles section: Following models define the dynamic roles.
"""

class Context(models.Model):
    """
    Defines the context or level for the group to operate on.
    For example, the organisation coordinator with context of 'organisation' 
    will have access to resources and activities at the organization level, 
    allowing them to manage and oversee operations within
    a specific organization.
    """
    name = models.CharField(max_length=200)

class UserGroup(models.Model):
    """
    This model stores mappings between users and groups for dynamic roles exclusively.
    It contains information regarding the contextual resource ID associated with the group.
    For example, if the training team creates a role such as 'School Test Reporter' with the school context, 
    this table will record the user assigned to this group and the corresponding 
    school ID in the 'school' column.
    When the value is set to 0 in a context column, it signifies access to all resources within that context. 
    For instance, a school value of 0 indicates that the user has access to test reports of all schools.
    """
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_groups")
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    organisation = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_group")
    state = models.ForeignKey(State, on_delete=models.PROTECT, related_name="user_group")
    district = models.ForeignKey(District, on_delete=models.PROTECT, related_name="user_group")
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name="user_group")
    school = models.ForeignKey(School, on_delete=models.PROTECT, related_name="user_group")
    classname = models.ForeignKey(ClassName, on_delete=models.PROTECT, related_name="user_group")
    section = models.ForeignKey(Section, on_delete=models.PROTECT, related_name="user_group")
    status = models.CharField(choices=APPROVAL_STATUS, max_length=100, default="pending_approval")
    approved_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)


"""
Dynamic roles section ends.
"""

"""
Message section: Following models define the message models.
"""

class MessageType(models.Model):
    TYPE_CHOICES = [
        ('Single Message', 'Single Message'),
        ('Bulk Message', 'Bulk Message'),
    ]
    messagetype = models.CharField(max_length=100, choices=TYPE_CHOICES)


class Message(models.Model):
    message = models.CharField(max_length=500, null=False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    sender_role = models.ForeignKey(
        Group, on_delete=models.CASCADE,
        related_name='sender_role'
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='received_messages'
    )
    receiver_role = models.ForeignKey(
        Group, on_delete=models.CASCADE,
        related_name='receiver_role'
    )
    message_type = models.ForeignKey(
        MessageType, on_delete=models.CASCADE,
        related_name='message_type'
    )

class Condition(models.Model):
    sender = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='receiver')
    single_msg = models.BooleanField(default=False)
    bulk_msg = models.BooleanField(default=False)

    class Meta:
        unique_together = ['sender', 'receiver']

"""
Message section ends.
"""

class Payment(models.Model):
    PAYMENT_CHOICES = [('IN_PROCESS', 'IN_PROCESS'), ('COMPLETED', 'COMPLETED'),]
    date_of_payment = models.DateField()
    amount = models.IntegerField()
    utr = models.CharField(max_length=200, unique=True)
    receipt = models.FileField(upload_to='receipts/')
    expiry_date = models.DateField()  # payment expiry
    status = models.CharField(max_length=50, choices=PAYMENT_CHOICES)
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT)
    added_by = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        ordering = ['date_of_payment']

    def __str__(self):
        return f"{self.school.name_of_association} - {self.date_of_payment}"