from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from accounts.models import Organisation, School
from accounts.serializers.institution_serializers import OrganisationSerializer, \
        SchoolSerializer


class OrganisationViewset(viewsets.ModelViewSet):
    """
    Viewset for the Organisation model.
    This viewset provides CRUD operations for Organisation objects.
    """
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a new Organisation object.

        This method handles the creation of a new Organisation object based on
        the provided data.

        Returns:
            Response: The serialized data of the created Organisation object
                      with status code 201 (Created).
        """
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        """
        Partially update an existing Organisation object.

        This method handles the partial update of an existing Organisation
        object based on the provided data.

        Args:
            request (Request): The HTTP request object.
            pk (int): The primary key of the Organisation object to be updated.

        Returns:
            Response: The serialized data of the updated Organisation object
                      with status code 200 (OK), or an error response with
                      status code 400 (Bad Request) if an exception occurs.
        """
        try:
            organisation = get_object_or_404(Organisation, pk=pk)
            serializer = self.serializer_class(organisation, data=request.data,
                                               partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class SchoolViewset(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def create(self, request, *args, **kwargs):
        print("SchoolViewset**")
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
