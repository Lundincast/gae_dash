from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ResourceDescriptorSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=500)
    display_name = serializers.CharField(max_length=500)
    description = serializers.CharField(max_length=500)
    name = serializers.CharField(max_length=500)