"""gae_dash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from metrics import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('env_var', views.environment_variables),
    path('monitored_resource_types', views.monitored_resource_types),
    path('application_details', views.application_details),
    path('services', views.services_list),
    path('services/<service>', views.service_details),
    path('services/<service>/versions', views.versions_list),
    path('services/<service>/versions/<version>', views.version_details),
    path('services/<service>/versions/<version>/instances', views.instances_list),
    path('services/<service>/versions/<version>/instances/<instance>', views.instance_details),
]
