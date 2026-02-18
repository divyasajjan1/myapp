from django.contrib import admin
from .models import Player

# Register your models here.
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('player_name', 'team', 'player_height', 'player_weight', 'player_matches_played')
    list_filter = ('team',)  # adds a filter sidebar for DC vs Marvel