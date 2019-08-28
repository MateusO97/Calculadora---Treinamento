from django.conf import settings
from django.db import models
from django.utils import timezone

class Operacao(models.Model):
    number1 = models.IntegerField()
    number2 = models.IntegerField()
    result = models.IntegerField()
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()