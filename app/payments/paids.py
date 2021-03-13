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

    def update(self, request):
        """recived data"""
        try:
            form_paid = Payment.objects.get(
                header=request.data.get("PedidoID"),
                status_pay=request.data.get("MetodoPago"),
            )
            form_paid.updated_at = (
                request.data.get("Fecha") + " " + request.data.get("Hora")
            )
            form_paid.status_pay = int(request.data.get("MetodoPago"))
            form_paid.save()

            return Response(
                {"data": True, "msg": "pay completed."}, status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response(
                {"data": False, "msg": f"{e}"}, status=status.HTTP_400_BAD_REQUEST
            )
