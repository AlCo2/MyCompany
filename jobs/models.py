from django.db import models

# Create your models here.

class Company(models.Model):
    boss = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    about = models.TextField()
    worker = models.IntegerField()
    started = models.DateField()
    value = models.IntegerField()
