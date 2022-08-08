from unicodedata import name
from django.db import models

# Create your models here.
class Repository(models.Model):
    name = models.TextField()
    version = models.TextField()