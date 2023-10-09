from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
from common.models import State, District, City, Language
from config import RESOURCES


MAX_CLASS = 12
CLASS_CHOICES = [(i, f"Class {i}") for i in range(1, MAX_CLASS+1)]


class User(AbstractUser):
    phone_regex = RegexValidator(regex=r'^(\+[1-9][0-9]*-)?[1-9][0-9]{6,}$',
                                 message='Enter a valid phone/mobile number')

    email = models.EmailField(unique=True, null=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=False,
                                  null=False)
    last_name = models.CharField(_("last name"), max_length=150, blank=False,
                                 null=False)
    phone = models.CharField(max_length=20, null=True, validators=[phone_regex])


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
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other'),
                      ('NA', 'Not applicable')]  # 'NA' in case of organisation & school

    user = models.ForeignKey(User, on_delete=models.PROTECT,
                             related_name='profile_info')
    dob = models.DateField(help_text='YYYY-MM-DD')
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    updated = models.DateField(auto_now=True)


class Organisation(models.Model):
    ASSOCIATION_CHOICES = [
        ('Central Government', 'Central Government'),
        ('State Government', 'State Government'),
        ('Public Company', 'Public Company'),
        ('Private Company', 'Private Company'),
        ('NGO', 'NGO'),
        ('Foreign', 'Foreign'),
    ]

    added_by = models.ForeignKey(User, on_delete=models.PROTECT,
                                 related_name='associated_organisation')
    name_of_association = models.CharField(max_length=200, unique=True)
    date_of_association = models.DateField()
    type = models.CharField(max_length=100, choices=ASSOCIATION_CHOICES)
    updated = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)

    class Meta:
        ordering = ['name_of_association', '-date_of_association']

    def __str__(self):
        return self.name_of_association


class School(models.Model):
    TYPE_CHOICES = [
        ('Central Government Funded', 'Central Government Funded'),
        ('State Government Funded', 'State Government Funded'),
        ('Public Company Funded', 'Public Company Funded'),
        ('Private Company Funded', 'Private Company Funded'),
        ('NGO Funded', 'NGO Funded'),
        ('Foreign Funded', 'Foreign Funded'),
        ('Self-Funded', 'Self-Funded'),
    ]

    added_by = models.ForeignKey(User, on_delete=models.PROTECT,
                                 related_name='school_added')
    name_of_association = models.CharField(max_length=200, unique=True)
    date_of_association = models.DateField()
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT,
                                     null=True, blank=True)
    updated = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)

    class Meta:
        ordering = ['name_of_association', '-date_of_association']

    def __str__(self):
        return self.name_of_association


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


class TrainingTeam(User):
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, null=True, blank=False)

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = 'Training Team'
        verbose_name_plural = 'Training Team'

    def __str__(self):
        return f"{self.username}"


class CentralCoordinator(User):
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, null=True, blank=False)
    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT)

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = 'Central Coordinator'
        verbose_name_plural = 'Central Coordinators'

    def __str__(self):
        return f"{self.username}"


class SchoolCoordinator(User):
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, null=True, blank=False)
    school = models.ForeignKey(School, on_delete=models.PROTECT)

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = 'School Coordinator'
        verbose_name_plural = 'School Coordinators'

    def __str__(self):
        return f"{self.username}"


class Teacher(User):
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, null=True, blank=False)
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    unique_id = models.CharField(max_length=50)

    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.username}"


class Parent(User):

    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.username}"


class Student(User):
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, null=True, blank=False)
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    unique_id = models.CharField(max_length=50)  # Enrolment ID / Any other unique ID
    preferred_lang = models.ForeignKey(Language, on_delete=models.PROTECT)
    current_class = models.IntegerField(choices=CLASS_CHOICES)
    division = models.CharField(max_length=50)
    _teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, related_name='students')
    _parent = models.ForeignKey(Parent, on_delete=models.PROTECT, related_name='children')

    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.username} - {self.school.name_of_association}"


class ClassCoordinator(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    classVal = models.IntegerField(choices=CLASS_CHOICES)

    class Meta:
        ordering = ['teacher__first_name', 'teacher__last_name']

    def __str__(self):
        return f"{self.teacher.username} - {self.classVal}"


class Condition(models.Model):
    sender = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='receiver')
    single_msg = models.BooleanField(default=False)
    bulk_msg = models.BooleanField(default=False)

    class Meta:
        unique_together = ['sender', 'receiver']


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


# Revised models
class Context(models.Model):
    """
    A context defines the level at which a role operates or an action is performed
    within the system. Example: Organization, city, class levels. It includes a name,
    description, and an order to define its level of hierarchy.

    Attributes:
        name (str): The name of the context.
        description (str): A detailed description of the context.
        order (int): The level of hierarchy for the context.

    Meta:
        ordering (list): The instances are ordered by their 'order' attribute in
        ascending order.

    Methods:
        __str__(): Returns a string representation of the context in the format
            'order - name'.
    """
    name = models.CharField(max_length=100, null=False, unique=True)
    description = models.TextField(null=False)
    order = models.IntegerField(null=False)  # Level of hierarchy

    def __str__(self):
        return f"{self.order} - {self.name}"

    class Meta:
        ordering = ['order']


class ContextAllowAssign(models.Model):
    """
    This model maintains a relationship between two Context instances,
    indicating that one context can assign roles in another context.

    Attributes:
        assigningLevel (ForeignKey): A ForeignKey relationship to the Context
            instance that has the permission to assign roles.
        assignedLevel (ForeignKey): A ForeignKey relationship to the Context
            instance where roles can be assigned.

    Meta:
        unique_together (list of str): The combination of 'assigningLevel' and
                                        'assignedLevel' must be unique.
        ordering (list of str): The default ordering of ContextAllowAssign
                                instances is by the
            'assigningLevel__order' and 'assignedLevel__order' attributes.
        db_table (str): The name of the database table for this model.

    Methods:
        __str__(): Returns a string representation of the permission.
    """
    assigningLevel = models.ForeignKey(Context, on_delete=models.CASCADE,
                                       related_name='assigningContext')
    assignedLevel = models.ForeignKey(Context, on_delete=models.CASCADE,
                                      related_name='assignedContext')

    class Meta:
        unique_together = ['assigningLevel', 'assignedLevel']
        ordering = ['assigningLevel__order', 'assignedLevel__order']
        db_table = 'accounts_context_allow_assign'

    def __str__(self):
        return f"{self.assigningLevel} can assign roles at level: {self.assignedLevel} "


class Permission(models.Model):
    """
    This model represents a permission within the system, which is used to
    control access to various resources.

    Attributes:
        name (str): The name of the permission. Example: 'Can add testimonials'.
        resource (str): The resource to which the permission is associated.
                        Example: 'testimonials', 'trainings'.
        description (str): A detailed description of the permission.

    Methods:
        __str__(): Returns a string representation of the permission.

    """
    RESOURCES = RESOURCES
    name = models.CharField(max_length=100, null=False, unique=True)
    resource = models.CharField(max_length=100, null=False, choices=RESOURCES)
    description = models.TextField(null=False)

    def __str__(self):
        return f"{self.name}"


class GroupPermission(models.Model):
    """
    This model defines that a specific role has a particular permission
    within a specific context.

    Attributes:
        role (ForeignKey to Group): The role (group) to which the permission
            is assigned.
        permission (ForeignKey to Permission): The permission being assigned to
            the role.
        context (ForeignKey to Context): The context in which the permission is
            granted.
        created (DateTimeField): The timestamp when this role-permission
            association was created.
        updated (DateTimeField): The timestamp when this role-permission
            association was last updated.

    Meta:
        unique_together (list of str): The combination of 'role' and
                                        'permission' must be unique.
        ordering (list of str): The default ordering of GroupPermission instances is
        by the 'role__name' and 'context__order' attributes.

    Methods:
        __str__(): Returns a string representation of the role-permission relationship.
    """
    role = models.ForeignKey(Group, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    context = models.ForeignKey(Context, on_delete=models.CASCADE)
    # ToDo For more granular control?
    # attribute = models.CharField(max_length=100, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['role', 'permission']
        ordering = ['role__name', 'context__order']

    def __str__(self):
        return f"{self.role} has permission {self.permission} at level: {self.context}"
