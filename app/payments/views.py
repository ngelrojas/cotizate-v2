from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.payment import Payment
from core.campaing import CampaingHeader
from .serializers import PaymentSerializer


class PaymentView(viewsets.ModelViewSet):
    """
    this view just create and update payment
    """

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def create(self, request):
        """
        rules to create a method payment:
        - campaing is public
        - user is activete and not deleted
        """
        try:
            current_campaing = CampaingHeader.objects.get(
                header=request.data.get("campaings")
            )
            data_send = {
                "name": request.data.get("name"),
                "amount": request.data.get("amount"),
                "type_pay": request.data.get("type_pay"),
                "status_pay": request.data.get("status_pay"),
                "users": request.user.id,
                "campaings": current_campaing.id,
            }
            serializer = self.serializer_class(data=data_send)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    {"data": "payment created."}, status=status.HTTP_201_CREATED
                )
        except CampaingHeader.DoesNotExist as err:
            return Response({"error": f"{err}"}, status=status.HTTP_404_NOT_FOUND)
