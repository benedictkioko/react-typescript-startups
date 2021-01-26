from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from django.contrib.auth.models import User

from .serializers import ScoreSerializer

from core.models import Score


class ScoreList(generics.ListCreateAPIView):
    """Creating and viewing of scores"""

    serializer_class = ScoreSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Score.objects.filter(owner=self.request.user)


class ScoreDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Fetching, updating and deleting scores"""

    serializer_class = ScoreSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "ScoreId"

    def get_queryset(self):
        return Score.objects.filter(owner=self.request.user)
