from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

import os

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
def env_variables(request):
    """
    API endpoint that retrieves available environment variables.
    """
    var_dict = {}
    for var in os.environ.keys():
        var_dict[var] = os.environ.get(var)
    return Response(var_dict)