from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import status
from rest_framework import viewsets
from accounts.serializers.user_serializers import *
    
class TrainingTeamViewSet(viewsets.ModelViewSet):
    serializer_class = TrainingTeamSerializer
    queryset = TrainingTeam.objects.all()
    permission_classes = (AllowAny,)
     
class CentralCoordinatorViewset(viewsets.ModelViewSet):
    serializer_class = CentralCoordinatorSerializer
    queryset = CentralCoordinator.objects.all()
    permission_classes = (AllowAny,)
    
class SchoolCoordinatorViewset(viewsets.ModelViewSet):
    serializer_class = SchoolCoordinatorSerializer
    queryset = SchoolCoordinator.objects.all()
    permission_classes = (AllowAny,)
    
class TeacherViewset(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    permission_classes = (AllowAny,)
    
class ParentViewset(viewsets.ModelViewSet):
    serializer_class = ParentSerializer
    queryset = Parent.objects.all()
    permission_classes = (AllowAny,)
    