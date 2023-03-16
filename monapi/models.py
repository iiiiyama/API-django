from django.db import models
from datetime import date
from rest_framework import serializers

class Commentaire (serializers.ModelSerializer):
    titre = models.CharField(max_length=50)
    commentaire = models.TextField()
    date = models.DateField(default=date.today())

# Create your models here.
