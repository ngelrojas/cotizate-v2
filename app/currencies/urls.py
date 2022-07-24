from django.urls import path
from .views import CurrencyView

app_name = "currency"

urlpatterns = [
        path("currency", CurrencyView.as_view({"get": "list"}),
            name="currency",
        )
]
