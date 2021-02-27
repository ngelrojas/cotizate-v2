from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.payment import Payment
from .serializers import PaymentSerializer


class PaidCallback(viewsets.ModelViewSet):
    """
    this view recived a response from provider payment
    """

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def create(self, request):
        """recived data"""
        try:
            form_paid = Payment.objects.get(
                company_payment_id=request.data.get("PedidoID")
            )
            form_paid.updated_at = (
                request.data.get("Fecha") + " " + request.data.get("Hora")
            )
            form_paid.status_pay = request.data.get("Estado")
            form_paid.save()

            return Response({"data": "paid completed."}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
