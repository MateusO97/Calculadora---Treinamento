from django.conf import settings
from django.db import models

class Operacao(models.Model):
    number1 = models.IntegerField()
    number2 = models.IntegerField()
    result = models.IntegerField()

    def armazena(self):
        self.save()
