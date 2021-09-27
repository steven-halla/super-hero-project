from django.db import models

# Create your models here.
class Superhero(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    alter_ego = models.CharField(max_length=50)
    primary_ability = models.CharField(max_length=50)
    secondary_abilith = models.CharField(max_length=50)
    catch_phrase = models.CharField(max_length=50)

    def __str__(self):
        return self.name