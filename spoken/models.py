from django.db import models
from accounts.models import User, APPROVAL_STATUS
from common.models import State, District

class NationalCoordinator(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="national_coord")
    status = models.CharField(choices=APPROVAL_STATUS, max_length=100)
    approved_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


class StateCoordinator(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="state_coord")
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    status = models.CharField(choices=APPROVAL_STATUS, max_length=100)
    approved_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

class DistrictCoordinator(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="district_coord")
    district = models.ForeignKey(District, on_delete=models.PROTECT)
    status = models.CharField(choices=APPROVAL_STATUS, max_length=100)
    approved_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

