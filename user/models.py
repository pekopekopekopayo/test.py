from django.db import models

# Create your models here.

class User(models.Model):
    account = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'user'