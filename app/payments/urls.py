from django.urls import path
from payments import views, paids
from payments.payment_view import PaymentView

app_name = "payment"

urlpatterns = [
    path("payment", PaymentView.as_view({"post": "create"}), name="payment"),
    path(
        "payment-recived",
        paids.PaidCallback.as_view({"post": "create"}),
        name="payment-recived",
    ),
]
