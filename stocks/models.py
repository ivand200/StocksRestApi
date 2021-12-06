from django.db import models

# Create your models here.
class Index(models.Model):
    name = models.CharField(max_length=20, db_index=True)

    def __str__(self):
        return self.name


class Stock(models.Model):
    ticker = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    momentum_12_2 = models.FloatField()
    momentum_avg = models.FloatField()
    ma10 = models.IntegerField()
    e_p = models.FloatField()
    div_p = models.FloatField()
    index = models.ForeignKey(Index, on_delete=models.CASCADE)

    def __str__(self):
        return self.ticker
