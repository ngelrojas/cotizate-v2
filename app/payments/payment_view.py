from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.payment import Payment
from .serializers import PaymentSerializer
from .helper.helperPay import HelperPay


class PaymentView(viewsets.ModelViewSet):
    """
    this view recived a response from provider payment
    """

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def create(self, request):
        """recived data"""
        try:
            resp = HelperPay.saving_payment(self, request)
            if resp is True:
                return Response(
                    {"data": True, "msg": "pay saved."}, status=status.HTTP_200_OK
                )

            return Response(
                {"data": False, "msg": f"{resp}"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response({"error": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
