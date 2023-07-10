from django.urls import path, include
from accounts.api.user_api import TrainingTeamViewSet
from accounts.api.institution_api import OrganisationViewset, SchoolViewset
from accounts.api.user_api import CentralCoordinatorViewset, SchoolCoordinatorViewset, \
     TeacherViewset, ParentViewset
from rest_framework import routers
from .views import LogoutView, MessageWithinCommunity
app_name = "accounts"

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'register/training-team', TrainingTeamViewSet,
                basename='training-team-register')
router.register(r'register/organisations', OrganisationViewset,
                basename='organisation-register')
router.register(r'register/schools', SchoolViewset, basename='school-register')
router.register(r'register/central-coordinators', CentralCoordinatorViewset,
                basename='central-coord-register')
router.register(r'register/school-coordinators', SchoolCoordinatorViewset,
                basename='central-coord-register')
router.register(r'register/teachers', TeacherViewset, basename='teacher-register')
router.register(r'register/parents', ParentViewset, basename='parent-register')

urlpatterns = [
     path('', include(router.urls)),
     path('logout/', LogoutView.as_view(), name='logout'),
     path('message-list', MessageWithinCommunity.as_view(), name='message-list'),
]
