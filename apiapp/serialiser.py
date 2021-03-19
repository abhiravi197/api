from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = [ 'id','url','name','age','phone','address' ]

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = post
        fields = ['id','url','title', 'content', 'author', 'publish']
