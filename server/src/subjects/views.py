from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from django.contrib.auth.models import User

from .serializers import SubjectSerializer

from core.models import Subject


class SubjectList(generics.ListCreateAPIView):
    """Creating and viewing od subjects"""

    serializer_class = SubjectSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Subject.objects.filter(owner=self.request.user)


class SubjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Creating and viewing od subjects"""

    serializer_class = SubjectSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "SubjectId"

    def get_queryset(self):
        return Subject.objects.filter(owner=self.request.user)
