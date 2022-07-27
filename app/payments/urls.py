from django.urls import path
from .views import PaymentView 

app_name = "payment"

urlpatterns = [
    path("payment",
        PaymentView.as_view({"post": "create"}), name="payment"),
    path(
        "payment-recived/<int:pk>",
        PaymentView.as_view({"put": "update"}),
        name="payment-recived",
    ),
]
