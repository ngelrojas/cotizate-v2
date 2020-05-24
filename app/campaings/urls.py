from django.urls import path
from campaings import views
from campaings import public

app_name = 'campaing'

urlpatterns = [
    path('campaing', views.CampaingView.as_view({
        'get': 'list',
        'post': 'create'}), name='campaing'),
    path('campaing/<int:pk>', views.CampaingView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'delete',
        'patch': 'patch'}), name='detail-campaing'),
    path('campaings', public.CampaingPublicView.as_view({
        'get': 'list'}), name='public-campaing')
]
