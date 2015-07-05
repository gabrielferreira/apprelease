from django.shortcuts import render
from rest_framework import viewsets
from .models import Application
from .serializers import ApplicationSerializer

# Create your views here.
# ViewSets define the view behavior.
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
