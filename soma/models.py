from django.db import models

class Soma(models.Model):
    number1 = models.IntegerField()
    number2 = models.IntegerField()
    result = models.IntegerField()

    def get_result(self):
        result = number1 + number2
        return self.result
        self.save()