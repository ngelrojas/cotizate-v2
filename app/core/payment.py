from django.db import models
from .campaing import CampaingHeader
from core.user import User


class Payment(models.Model):
    """model payment"""

    TYPE_PAY = ((1, "credit"), (2, "debit"), (3, "cash"))
    STATUS_PAY = ((1, "pending"), (2, "complete"), (3, "rejected"))

    total_amount = models.DecimalField(max_digits=12, decimal_places=3)
    title_campaing = models.CharField(max_length=200)
    number_card = models.CharField(max_length=20)
    company_payment_name = models.CharField(max_length=100)
    company_payment_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    type_pay = models.IntegerField(choices=TYPE_PAY)
    status_pay = models.IntegerField(choices=STATUS_PAY)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.ForeignKey(CampaingHeader, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
