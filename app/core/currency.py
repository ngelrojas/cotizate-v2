from django.db import models


class Currency(models.Model):
    """model currency"""
    name = models.CharField(max_length=20, default='Boliviano')
    symbol = models.CharField(max_length=5, default='$BS')

    def __str__(self):
        return self.name
