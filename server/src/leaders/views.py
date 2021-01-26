from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from django.contrib.auth.models import User

from .serializers import LeaderSerializer

from core.models import Leader


class LeaderList(generics.ListCreateAPIView):
    """Creating and viewing of leaders"""

    serializer_class = LeaderSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Leader.objects.filter(owner=self.request.user)


class LeaderDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Fetching, updating and deleting leaders"""

    serializer_class = LeaderSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "LeaderId"

    def get_queryset(self):
        return Leader.objects.filter(owner=self.request.user)
