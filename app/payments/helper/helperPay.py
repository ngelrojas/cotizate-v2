from core.payment import Payment
from core.campaing import CampaingHeader


class HelperPay:
    """help to save and update payments"""

    def saving_payment(self, request):
        """saveing payment from current user"""
        try:
            lcpedidoid = CampaingHeader.objects.get(id=request.data.get("lcpedidoid"))
            Payment.objects.create(
                total_amount=request.data.get("lnmonto"),
                user=request.user,
                header=lcpedidoid,
                coin=int(request.data.get("lcmoneda")),
            )
            return True
        except Exception as e:
            return e
