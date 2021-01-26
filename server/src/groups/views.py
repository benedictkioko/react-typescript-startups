from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from django.contrib.auth.models import User

from .serializers import GroupSerializer

from core.models import Group


class GroupList(generics.ListCreateAPIView):
    """Creating and viewing of groups"""

    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Group.objects.filter(owner=self.request.user)


class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Fetching, updating and deleting of groups"""

    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "GroupId"

    def get_queryset(self):
        return Group.objects.filter(owner=self.request.user)
