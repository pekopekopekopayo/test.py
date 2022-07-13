from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey('user.User', related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    class Meta:
        db_table = 'item'