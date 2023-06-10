from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from accounts.serializers.user_serializers import TrainingTeamSerializer, \
    CentralCoordinatorSerializer, SchoolCoordinatorSerializer, SchoolCoordinator, \
    TeacherSerializer, ParentSerializer
from accounts.models import TrainingTeam, CentralCoordinator, Teacher, Parent


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
