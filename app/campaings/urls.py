from django.urls import path
from .views import Campaings
from .public import CampaingPublic, CampaingCompleted, CampaingTerminated

app_name = 'campaing-app'

urlpatterns = [
    path('campaing', Campaings.as_view({
        'get': 'list',
        'post': 'create'}), name='campaing'),

    path('campaing/<int:pk>', Campaings.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'delete'}), name='detail-campaing'),

    path('campaing-public', CampaingPublic.as_view({
        'get': 'list'}), name='public-campaing'),

    path('campaing-completed', CampaingCompleted.as_view({
        'get': 'list'}), name='complete-campaing'),

    path('campaing-terminated', CampaingTerminated.as_view({
        'get': 'list'}), name='terminated-campaing'),
]
