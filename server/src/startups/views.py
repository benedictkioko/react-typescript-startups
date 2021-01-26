from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from django.contrib.auth.models import User

from .serializers import StudentSerializer

from core.models import Student


class StudentsList(generics.ListCreateAPIView):
    """Creating and viewing od students"""

    serializer_class = StudentSerializer
    # authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Student.objects.filter(owner=self.request.user)


class StudentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Creating and viewing od students"""

    serializer_class = StudentSerializer
    # authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "StudentId"

    def get_queryset(self):
        return Student.objects.filter(owner=self.request.user)
