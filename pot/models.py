from django.db import models


# Create your models here.
class Pot(models.Model):
    number_x = models.IntegerField()
    number_y = models.IntegerField()
    result = models.IntegerField()

    def potentiation(self):
        self.result = self.number_x ** self.number_y
