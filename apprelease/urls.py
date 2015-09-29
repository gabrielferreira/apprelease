"""apprelease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from rest_framework import routers
from django.contrib import admin
# from release import views
from rest_framework.authtoken import views as restviews


from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
for user in User.objects.all():
    Token.objects.get_or_create(user=user)

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'applications', views.ApplicationViewSet)
# router.register(r'releases', views.ReleaseViewSet)
# router.register(r'flavours', views.FlavourViewSet)
# router.register(r'platforms', views.PlatformViewSet)
# router.register(r'environments', views.EnvironmentViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', restviews.obtain_auth_token),
    # url(r'^applications', 'release.views.view_applications', name='view_applications'),
    # url(r'^environments/(?P<application>[0-9]+)/$', views.view_environments, name='view_environments'),
    # url(r'^releases/(?P<application>[0-9]+)/$', views.view_releases_by_application, name='view_releases_by_application'),
    # url(r'^release/(?P<release>[0-9]+)/$', views.view_release, name='view_release'),
]
