from django.db import models
from .campaing import Campaing
from core.user import User


class Payment(models.Model):
    """model payment"""

    TYPE_PAY = (
        (1, "TigoMoney"),
        (2, "PuntoPagoFacil"),
        (3, "TarjetaDebito/Credito-Enlace"),
        (4, "TransferenciaBancosQR"),
        (5, "BCP-RAPIDO-SEGURO"),
        (6, "LINKSER"),
    )
    STATUS_PAY = (
        (1, "pending/in-process"),
        (2, "paid"),
        (3, "reversed"),
        (4, "canceled"),
    )
    COIN = ((1, "USD"), (2, "BOB"))

    total_amount = models.DecimalField(max_digits=12, decimal_places=3)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    type_pay = models.IntegerField(choices=TYPE_PAY, default=1)
    status_pay = models.IntegerField(choices=STATUS_PAY, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.ForeignKey(Campaing, on_delete=models.CASCADE)
    encrypted_parameter = models.TextField(default="0")
    commerce_id = models.TextField(default="0")
    coin = models.IntegerField(choices=COIN, default=2)
    transaction_id = models.IntegerField(default=0)

    def __str__(self):
        return self.user.first_name
