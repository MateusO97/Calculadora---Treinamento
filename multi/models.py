from django.db import models

# Create your models here.
class Multi(models.Model):
    number_x = models.IntegerField(null = False)
    number_y = models.IntegerField(null = False)
    res = models.IntegerField(null = False)

    def __init__(self):
        self.multi()

    def multi(self, x = 0, y = 0):
        self.number_x = x
        self.number_y = y
        self.res = self.number_x * self.number_y    
