from django.urls import path
from .views import FavoriteView

app_name = 'favorite'

urlpatterns = [
    path('favorite', FavoriteView.as_view({
        'get': 'list',
        'post': 'create'}), name='favorite'),
    path('favorite/<int:pk>', FavoriteView.as_view({
        'get': 'retrieve',
        'put': 'update'}), name='detail-favorite'),
]
