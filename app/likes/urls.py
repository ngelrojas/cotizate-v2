from django.urls import path
from .views import LikeView

app_name = 'like'

urlpatterns = [
    path('like', LikeView.as_view({
        'get': 'list',
        'post': 'create'}), name='like'),
    path('like/<int:pk>', LikeView.as_view({
        'get': 'retrieve',
        'put': 'update'}), name='detail-like'),
]
