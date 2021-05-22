from django.urls import path
from denounces import views
from denounces import public

app_name = "denounces"

urlpatterns = [
    path(
        "denounces",
        views.DenounceView.as_view({"get": "list", "post": "create"}),
        name="denounces",
    ),
    path(
        "denounces/<int:pk>",
        views.DenounceView.as_view({"get": "retrieve"}),
        name="denounces-list",
    ),
    path(
        "denounces/public",
        public.DenouncePublicView.as_view({"post": "create"}),
        name="denounces-public",
    ),
]
