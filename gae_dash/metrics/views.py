from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from metrics.serializers import UserSerializer, GroupSerializer, ResourceDescriptorSerializer

from google.cloud import monitoring_v3
from google.auth import compute_engine
from google.auth.transport.requests import AuthorizedSession

from rest_framework.decorators import api_view
from rest_framework.response import Response

import os
import requests
import json
from datetime import datetime, timedelta

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@api_view(['GET'])
def environment_variables(request):
    """
    API endpoint that retrieves available environment variables.
    """
    var_dict = {}
    for var in os.environ.keys():
        var_dict[var] = os.environ.get(var)
    return Response(var_dict)


@api_view(['GET'])
def monitored_resource_types(request):
    """
    API endpoint that lists the monitored resource types.
    """
    client = monitoring_v3.MetricServiceClient()
    project_name = client.project_path("digaaa-staging")

    resource_descriptors = list()

    for element in client.list_monitored_resource_descriptors(project_name):
        # process element
        obj = monitored_resource_descriptor(element.type, element.display_name, element.description, element.name)
        resource_descriptors.append(obj)

    serializer = ResourceDescriptorSerializer(resource_descriptors, many=True)
    return Response(serializer.data)


class monitored_resource_descriptor(object):
    def __init__(self, type, display_name, description, name):
        self.type = type
        self.display_name = display_name
        self.description = description
        self.name = name


@api_view(['GET'])
def application_details(request):
    """
    API endpoint that gets information about the running application
    """
    credentials = compute_engine.Credentials()
    authed_session = AuthorizedSession(credentials)

    res = authed_session.get('https://appengine.googleapis.com/v1/apps/{}'.format(os.environ.get("GOOGLE_CLOUD_PROJECT")))

    return Response(res.json())


@api_view(['GET'])
def services_list(request):
    """
    API endpoint that lists the services for the current application
    """
    credentials = compute_engine.Credentials()
    authed_session = AuthorizedSession(credentials)

    res = authed_session.get('https://appengine.googleapis.com/v1/apps/{}/services'.format(os.environ.get("GOOGLE_CLOUD_PROJECT")))

    return Response(res.json())


@api_view(['GET'])
def service_details(request, service):
    """
    API endpoint that lists the services for the current application
    """
    credentials = compute_engine.Credentials()
    authed_session = AuthorizedSession(credentials)

    res = authed_session.get('https://appengine.googleapis.com/v1/apps/{}/services/{}'.format(os.environ.get("GOOGLE_CLOUD_PROJECT"), service))

    return Response(res.json())


@api_view(['GET'])
def versions_list(request, service):
    """
    API endpoint that lists the versions of a service
    """
    credentials = compute_engine.Credentials()
    authed_session = AuthorizedSession(credentials)

    res = authed_session.get('https://appengine.googleapis.com/v1/apps/{}/services/{}/versions'.format(os.environ.get("GOOGLE_CLOUD_PROJECT"), service))

    return Response(res.json())


@api_view(['GET'])
def version_details(request, service, version):
    """
    API endpoint that lists the versions of a service
    """
    credentials = compute_engine.Credentials()
    authed_session = AuthorizedSession(credentials)

    res = authed_session.get('https://appengine.googleapis.com/v1/apps/{}/services/{}/versions/{}'.format(os.environ.get("GOOGLE_CLOUD_PROJECT"), service, version))

    return Response(res.json())


@api_view(['GET'])
def instances_list(request, service, version):
    """
    API endpoint that lists the versions of a service
    """
    credentials = compute_engine.Credentials()
    authed_session = AuthorizedSession(credentials)

    res = authed_session.get('https://appengine.googleapis.com/v1/apps/{}/services/{}/versions/{}/instances'.format(os.environ.get("GOOGLE_CLOUD_PROJECT"), service, version))

    return Response(res.json())


@api_view(['GET'])
def instance_details(request, service, version, instance):
    """
    API endpoint that lists the versions of a service
    """
    credentials = compute_engine.Credentials()
    authed_session = AuthorizedSession(credentials)

    res = authed_session.get('https://appengine.googleapis.com/v1/apps/{}/services/{}/versions/{}/instances/{}'.format(os.environ.get("GOOGLE_CLOUD_PROJECT"), service, version, instance))

    return Response(res.json())