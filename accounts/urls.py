from django.urls import path, include
from .api import *

from rest_framework import routers
app_name="accounts"

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'register/training-team', TrainingTeamViewSet,basename='training-team-register')
urlpatterns = [
     path('', include(router.urls)),
]