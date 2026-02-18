from django.shortcuts import render
from .models import Player
from .serializers import PlayerSerializer
from rest_framework import viewsets

# Create your views here.
class TeamDCViewset(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer

    def get_queryset(self):
        return Player.objects.filter(team="DC")
    def perform_create(self, serializer):
        serializer.save(team="DC")

class TeamMarvelViewset(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer

    def get_queryset(self):
        return Player.objects.filter(team="Marvel")
    def perform_create(self, serializer):
        serializer.save(team="Marvel")