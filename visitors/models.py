from django.db import connections
from django.db import models

# Create your models here.

class Visitor(models.Model):   
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    class Meta:
        db_table = "visitors"


