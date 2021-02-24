from django.urls import path
from payments import views

app_name = "payment"

urlpatterns = [
    path("payment", views.PaymentView.as_view({"post": "create"}), name="payment"),
]
