from django.db import models

# Create your models here.
class Multi(models.Model):
    number_x = models.IntegerField(null = False)
    number_y = models.IntegerField(null = False)
    res = models.IntegerField(null=False)