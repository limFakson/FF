from django.db import models
from django.contrib.auth.models import User

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    domain_url = models.CharField(max_length=100, unique=True)
    db_name = models.CharField(max_length=100, unique=True)
    db_user = models.CharField(max_length=100)
    db_password = models.CharField(max_length=100)
    db_host = models.CharField(max_length=100, default='localhost')
    db_port = models.CharField(max_length=5, default='3306')

    def __str__(self):
        return self.name

