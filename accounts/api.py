from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import status
from rest_framework import viewsets
from .serializers import *
    
class TrainingTeamViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the TrainingTeam model.
    """
    serializer_class = TrainingTeamSerializer
    queryset = TrainingTeam.objects.all()
    permission_classes = (AllowAny,)
    
    http_method_names = ['post','get','patch']
    
    def retrieve(self, request, pk=None):
        """
        Retrieve a specific TrainingTeam instance.
        """
        user = get_object_or_404(TrainingTeam, pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def list(self, request):
        """
        Retrieve a list of TrainingTeam instances.
        """
        serializer = self.serializer_class(self.queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    def create(self,request):
        """
        Create a new TrainingTeam instance.
        """
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            tt = serializer.save()
            return Response({"training_team" : serializer.data,},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        
    def update(self,request,pk=None):
        """
        Update a specific TrainingTeam instance.
        """
        try:
            training_team = get_object_or_404(TrainingTeam,pk=pk)
            serializer = self.serializer_class(training_team,data=request.data,partial=True)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def partial_update(self, request, pk=None):
        """
        Partially update a specific TrainingTeam instance.
        """
        return self.update(request, pk=pk)