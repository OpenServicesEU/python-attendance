from rest_framework import viewsets

from . import (
    serializers,
    models,
)


class StudentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


class EntryViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = models.Entry.objects.all()
    serializer_class = serializers.EntrySerializer
