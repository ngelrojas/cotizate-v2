from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.payment import Payment
from core.campaing import Campaing
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
            for item in request.data:
                header_id = Campaing.objects.get(id=item.get("PedidoID"))
                form_paid = Payment.objects.get(
                    header=header_id,
                    type_pay=item.get("MetodoPago"),
                    status_pay=1,
                )

                form_paid.updated_at = item.get("Fecha") + " " + item.get("Hora")

                form_paid.status_pay = int(item.get("Estado"))
                form_paid.save()

            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"data": False, "msg": f"{e}"}, status=status.HTTP_400_BAD_REQUEST
            )
