from django.db import models

# Create your models here.

class Etf(models.Model):
    ticker = models.CharField(max_length=20)
    momentum_12_1 = models.FloatField()
    momentum_avg = models.FloatField()
    momentum_3 = models.FloatField(null=True)
    ma10 = models.FloatField()

    def __str__(self):
        return self.ticker
