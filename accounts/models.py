from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from common.models import State, District, City, Language

MAX_CLASS = 10
CLASS_CHOICES = [ (i,f"Class {i}") for i in range(1,MAX_CLASS+1)]

class User(AbstractUser):
    email = models.EmailField(unique=True,blank=True,null=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=False, null=False)
    last_name = models.CharField(_("last name"), max_length=150, blank=False, null=False)

class Location(models.Model):
    """
        Complete address for users
    """
    address = models.TextField()
    state = models.ForeignKey(State,on_delete=models.PROTECT)
    district = models.ForeignKey(District,on_delete=models.PROTECT)
    city = models.ForeignKey(City,on_delete=models.PROTECT)
    pincode = models.CharField(max_length=6)
    updated = models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.address}, {self.district}, {self.city}, {self.state} - {self.pincode}"
    
class Profile(models.Model):
    """
        Profile information for users
    """
    phone_regex = RegexValidator(regex=r'^\+?[0-9]+-?[0-9]{6,}$',message='Enter a valid phone/mobile number')
    pincode_regex = RegexValidator(regex=r'^\d{6}$',message='Enter a valid pincode')
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'),('O', 'Other'),('NA','Not applicable')] # 'NA' in case of organisation & school

    user = models.ForeignKey(User,on_delete=models.PROTECT,related_name='profile')
    dob = models.DateField(help_text='YYYY-MM-DD')
    gender = models.CharField(max_length=2,choices=GENDER_CHOICES)
    phone = models.CharField(max_length=20,validators=[phone_regex])
    location = models.ForeignKey(Location, on_delete=models.PROTECT)    
    updated = models.DateField(auto_now=True)
    
class Organisation(models.Model):
    ASSOCIATION_CHOICES = [
    ('Central Government','Central Government'),
    ('State Government','State Government'),
    ('Public Company','Public Company'),
    ('Private Company','Private Company'),
    ('NGO','NGO'),
    ('Foreign','Foreign'),
    ]
    
    added_by = models.ForeignKey(User,on_delete=models.PROTECT)
    name_of_association = models.CharField(max_length=200,unique=True)
    date_of_association = models.DateField()
    type = models.CharField(max_length=100,choices=ASSOCIATION_CHOICES)
    updated = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    
    class Meta:
        ordering = ['name_of_association','-date_of_association']
    
    def __str__(self):
        return self.name_of_association
    
    
    
class School(models.Model):
    TYPE_CHOICES = [
        ('Central Government Funded','Central Government Funded'),
        ('State Government Funded','State Government Funded'),
        ('Public Company Funded','Public Company Funded'),
        ('Private Company Funded','Private Company Funded'),
        ('NGO Funded','NGO Funded'),
        ('Foreign Funded','Foreign Funded'),
        ('Self-Funded','Self-Funded'),
    ]
    
    added_by = models.ForeignKey(User,on_delete=models.PROTECT)
    name_of_association = models.CharField(max_length=200,unique=True)
    date_of_association = models.DateField()
    type = models.CharField(max_length=100,choices=TYPE_CHOICES)
    organisation = models.ForeignKey(Organisation,on_delete=models.PROTECT,null=True,blank=True)
    updated = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    
    class Meta:
        ordering = ['name_of_association','-date_of_association']
    
    def __str__(self):
        return self.name_of_association
    
class Payment(models.Model):
    PAYMENT_CHOICES = [('IN_PROCESS','IN_PROCESS'),('COMPLETED','COMPLETED'),]
    date_of_payment = models.DateField()
    amount = models.IntegerField()
    utr = models.CharField(max_length=200,unique=True)
    receipt = models.FileField(upload_to='receipts/')
    expiry_date = models.DateField() #payment expiry
    status = models.CharField(max_length=50,choices=PAYMENT_CHOICES)
    school = models.ForeignKey(School,on_delete=models.PROTECT)
    organisation = models.ForeignKey(Organisation,on_delete=models.PROTECT)
    added_by = models.ForeignKey(User,on_delete=models.PROTECT)
    
    class Meta:
        ordering = ['date_of_payment']

    def __str__(self):
        return f"{self.school.name_of_association} - {self.date_of_payment}"

class TrainingTeam(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    profile = models.ForeignKey(Profile,on_delete=models.PROTECT)
    class Meta:
        ordering = ['user__first_name','user__last_name']
        verbose_name = 'Training Team'
        verbose_name_plural = 'Training Team'
        
    def __str__(self):
        return f"{self.user.username}"

class CentralCoordinator(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    profile = models.ForeignKey(Profile,on_delete=models.PROTECT)
    organisation = models.ForeignKey(Organisation,on_delete=models.PROTECT)
    
    class Meta:
        ordering = ['user__first_name','user__last_name']
        verbose_name = 'Central Coordinator'
        verbose_name_plural = 'Central Coordinators'
        
    def __str__(self):
        return f"{self.user.username}"
    
class SchoolCoordinator(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    profile = models.ForeignKey(Profile,on_delete=models.PROTECT)
    school = models.ForeignKey(School,on_delete=models.PROTECT)
    
    class Meta:
        ordering = ['user__first_name','user__last_name']
        verbose_name = 'School Coordinator'
        verbose_name_plural = 'School Coordinators'
    
    def __str__(self):
        return f"{self.user.username}"
    
class Teacher(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    profile = models.ForeignKey(Profile,on_delete=models.PROTECT)
    school = models.ForeignKey(School,on_delete=models.PROTECT)
    unique_id = models.CharField(max_length=50)
    # classVal = models.ManyToManyField
    
    class Meta:
        ordering = ['user__first_name','user__last_name']
        
    def __str__(self):
        return f"{self.user.username}"
    
class Parent(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    
    class Meta:
        ordering = ['user__first_name','user__last_name']
        
    def __str__(self):
        return f"{self.user.username}"
    
class Student(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    profile = models.ForeignKey(Profile,on_delete=models.PROTECT)
    school = models.ForeignKey(School,on_delete=models.PROTECT)
    unique_id = models.CharField(max_length=50) #Enrolment ID / Any other unique ID
    preferred_lang = models.ForeignKey(Language,on_delete=models.PROTECT)
    current_class = models.IntegerField(choices=CLASS_CHOICES)
    division = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher,on_delete=models.PROTECT)
    parent = models.ForeignKey(Parent,on_delete=models.PROTECT)
    
    class Meta:
        ordering = ['user__first_name','user__last_name']
        
    def __str__(self):
        return f"{self.user.username} - {self.school.name_of_association}"
 
class ClassCoordinator(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.PROTECT)
    classVal =  models.IntegerField(choices=CLASS_CHOICES)
    
    class Meta:
        ordering = ['teacher__user__first_name','teacher__user__last_name']
        
    def __str__(self):
        return f"{self.teacher.user.username} - {self.classVal}"
    




    
    
    
    