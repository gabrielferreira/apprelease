from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Application, Platform, Flavour, Release, Environment
from .serializers import ApplicationSerializer, ReleaseSerializer, FlavourSerializer, EnvironmentSerializer, PlatformSerializer

# Create your views here.
# ViewSets define the view behavior.
class ApplicationViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ReleaseViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer

class FlavourViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Flavour.objects.all()
    serializer_class = FlavourSerializer

class EnvironmentViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer

class PlatformViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

def view_applications(request):
    return render_to_response('view_applications.html', {
        'applications': Application.objects.all()
    })

def view_environments(request, application):
    return render_to_response('view_environments.html', {
        'environments': Environment.objects.filter(application__id=application).all()
    })

def view_releases_by_application(request, application):
    return render_to_response('view_releases.html', {
        'releases': Release.objects.filter(environment__application__id=application).all()
    })
