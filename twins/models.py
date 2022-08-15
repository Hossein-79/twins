from pyexpat import model
from django.db import models

# Create your models here.
class Application(models.Model):
    repository_name = models.CharField(max_length=50)
    owner_name = models.CharField(max_length=50)
    contract_id = models.CharField(max_length=10)
    commit_id = models.CharField(max_length=50)
    expired = models.BooleanField()
    badge = models.CharField(max_length=50)
    check_date = models.DateField(auto_now=False, auto_now_add=True)
    last_check = models.DateField(auto_now=True, auto_now_add=False)