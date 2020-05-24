from django.db import models
from .campaing import Campaing


class Payment(models.Model):
    """model payment"""
    TYPE_PAY = (
        (1, 'credit'),
        (2, 'debit'),
        (3, 'cash')
    )
    STATUS_PAY = (
        (1, 'pending'),
        (2, 'complete'),
        (3, 'rejected')
    )
    name = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=12, decimal_places=3)
    created_at = models.DateTimeField(auto_now=True)
    type_pay = models.IntegerField(choices=TYPE_PAY)
    status_pay = models.IntegerField(choices=STATUS_PAY)
    users = models.IntegerField()
    campaings = models.ForeignKey(
        Campaing,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
