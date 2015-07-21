from django.shortcuts import render
from rest_framework import viewsets
from .models import Application, Platform, Flavour, Release, Environment
from .serializers import ApplicationSerializer, ReleaseSerializer, FlavourSerializer, EnvironmentSerializer, PlatformSerializer

# Create your views here.
# ViewSets define the view behavior.
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
class ApplicationViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer

class FlavourViewSet(viewsets.ModelViewSet):
    queryset = Flavour.objects.all()
    serializer_class = FlavourSerializer

class EnvironmentViewSet(viewsets.ModelViewSet):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer

class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
