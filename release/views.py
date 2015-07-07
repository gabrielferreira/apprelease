from django.shortcuts import render
from rest_framework import viewsets
from .models import Application, Release
from .serializers import ApplicationSerializer, ReleaseSerializer

# Create your views here.
# ViewSets define the view behavior.
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer
