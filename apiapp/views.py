from django.shortcuts import render
from rest_framework import viewsets
from apiapp.serialiser import UserSerializer,ProfileSerializer,PostSerializer
from django.contrib.auth.models import User
from .models import *
from rest_framework import permissions
from .permissions import IsAuthor


class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes = [permissions.IsAdminUser]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes = [permissions.IsAdminUser]

class PostViewSet(viewsets.ModelViewSet):
    queryset = post.objects.get_queryset().order_by('id')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated,IsAuthor]

    # def get_queryset(self):
    #     if self.request.user.is_authenticated:
    #         return posts.objects.all()
    #     return None
