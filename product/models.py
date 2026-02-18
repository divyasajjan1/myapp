from django.db import models


class Player(models.Model):
    id = models.BigAutoField(primary_key=True)
    team = models.CharField(max_length=20)
    player_name = models.CharField(max_length=100, db_column="name")
    player_height = models.FloatField(db_column="height")
    player_weight = models.FloatField(db_column="weight")
    player_matches_played = models.IntegerField(db_column="games")

    class Meta:
        db_table = "players"   # <-- must match existing table name
        managed = False        # <-- Don't try to create or modify this table.


