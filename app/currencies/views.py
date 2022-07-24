from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.currency import Currency
from .serializers import CurrencySerializer


class CurrencyView(viewsets.ModelViewSet):
    """list of currencies"""
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()

    def list(self, request):
        """get all currencies"""
        resp = Currency.objects.all()
        serializer = self.serializer_class(resp, many=True)
        return Response(
                {"data": serializer.data},
                status=status.HTTP_200_OK
        )

