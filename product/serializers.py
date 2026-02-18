from rest_framework import serializers
from .models import Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'team', 'player_name', 'player_height', 'player_weight', 'player_matches_played']
        read_only_fields = ['team']  