from django.urls import path
from .views import RewardView
from .public import RewardPublic

app_name = 'reward'

urlpatterns = [
    path('reward', RewardView.as_view({
        'get': 'list',
        'post': 'create'}), name='reward'),
    path('reward/<int:pk>', RewardView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'delete'}), name='reward-detail'),
    path('reward-public', RewardPublic.as_view({
        'get': 'list'}), name='public-reward'),
]
