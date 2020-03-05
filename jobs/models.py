from django.db import models

# Create your models here.
class Job(models.Model): # Create the new class here in python
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200, default='')