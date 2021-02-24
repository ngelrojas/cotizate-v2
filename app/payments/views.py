import hashlib
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.payment import Payment
from .serializers import PaymentSerializer
from .helper.pagofacilcheckoutclient import Checkout
from .helper.encriptacion import cryp3DES


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

            lcPedidoID = request.data.get("PedidoDeVenta")
            lcEmail = request.data.get("Email")
            lnTelefono = request.data.get("Celular")
            lnMonto = request.data.get("Monto")
            lcMoneda = request.data.get("Moneda")
            lcParametro1 = (
                "url callback (para retornar al comercio que se realizo un pago de su servicio o producto)",
            )
            lcParametro2 = (
                "url return (pagina de retorno para el cliente fina, pagina de confirmacion de compra)",
            )

            lcParametro3 = ""
            lcParametro4 = "11"
            commerce_vars = Checkout.sercret_var(self)
            tcCommerceID = commerce_vars["commerce_id"]
            lcTokenServicio = commerce_vars["token_service"]
            lcTokenSecret = commerce_vars["token_secret"]

            lcCadenaFirmar1 = f"{lcTokenServicio}|{lcEmail}|{lnTelefono}|{lcPedidoID}"
            lcCadenaFirmar2 = f"|{lnMonto}|{lcMoneda}|{lcParametro1}"
            lcCadenaFirmar3 = f"|{lcParametro2}|{lcParametro3}|{lcParametro4}"
            lcCadenaAFirmar = lcCadenaFirmar1 + lcCadenaFirmar2 + lcCadenaFirmar3

            # encoded before hashing
            var_signed = Checkout(lcCadenaAFirmar)
            # lcCadenaAFirmar = lcCadenaAFirmar4.encode()
            lcFirma = var_signed.hashing_string()
            # hashing
            # lcFirma = hashlib.sha256(lcCadenaAFirmar)

            lcDatosPago1 = f"{lcFirma}|{lcEmail}|{lnTelefono}|{lcPedidoID}|{lnMonto}"
            lcDatosPago2 = f"|{lcMoneda}|{lcParametro1}|{lcParametro2}"
            lcDatosPago3 = f"|{lcParametro3}|{lcParametro4}"

            lcDatosPago = lcDatosPago1 + lcDatosPago2 + lcDatosPago3
            # tcParametros = cryp3DES.encrypt_3des(self, lcDatosPago, lcTokenSecret)
            tcParametros = "YzBoTnUrWGxCM1FCcTI3YjF2RFFrcmdaN1hpWG85bmxxU0wxQjgzVjBQMVlRMU5Ka01NVTE1b3lDamNCdmcvMXZJNHVxQXFUNEFRRDVZVVNDcmNSSkRDTGVIVkd5RGNSYVQ1c2t5bFhteWJuVmxMbUNlbUNFd0dQeW5GVTM2eUk5cjRMWTFwcisvMnBGenhUSDh1RWpjZ0wrZFEzWUxNZ3ZkL2tNY0JEcWd0RDBuTWoxMk1rQlR1STBZNTNZYnBpQ2JvSzRTNnJOTTgxYXVZWGJTWFVZL1N4S2YwckliSWV0b1ZKSU1jcnFETmxxZHlEOW9XaGE0a2lRRzZadm94RW9GYnJNaHdZdCtMMjJxQ2I0QlVrSUMvQkFJajROQ2JoNkdxWktXL21KcjRoc202WEdDN0YrUWZ4NE0xSzhjSjlZVFgvait5dEY2UEJhM0xHbGJBNlM4bEJQS0ZhaUFnOEc4QzU2bW8yN1ovanYvZytCZWQrcFgyeWltSmRxT0R5QTFHKzA3SVQyT1puRDU2NDAzZXVqL1Q5ems5WmNzV3hYK2c3VUl4bVJObUJzdUkyODF5N0NRPT0="
            DtcParametros = cryp3DES.decrypt_3des(self, tcParametros, lcTokenSecret)

            laData = {"tcParametros": DtcParametros, "tcCommerceID": tcCommerceID}

            return Response({"data": laData}, status=status.HTTP_200_OK)

        except Exception as err:
            return Response({"error": f"{err}"}, status=status.HTTP_404_NOT_FOUND)
