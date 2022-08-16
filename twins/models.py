from pyexpat import model
from django.db import models

# Create your models here.
class Application(models.Model):
    repository_name = models.CharField(max_length=64)
    owner_name = models.CharField(max_length=64)
    contract_id = models.CharField(max_length=10)
    commit_hash = models.CharField(max_length=64)
    expired = models.BooleanField()
    check_date = models.DateField(auto_now=False, auto_now_add=True)