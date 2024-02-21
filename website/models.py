from django.db import models

# Create your models here.
class Post(models.Model):
    description = models.CharField(max_length=30000)