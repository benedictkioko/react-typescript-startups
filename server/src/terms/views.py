from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from django.contrib.auth.models import User

from .serializers import TermSerializer

from core.models import Term


class TermList(generics.ListCreateAPIView):
    """Creating and viewing of terms"""

    serializer_class = TermSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Term.objects.filter(owner=self.request.user)


class TermDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Fetching, updating and deleting terms"""

    serializer_class = TermSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "TermId"

    def get_queryset(self):
        return Term.objects.filter(owner=self.request.user)
