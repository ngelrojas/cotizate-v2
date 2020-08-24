from django.urls import path
from .views import Campaings
# from .public import CampaingPublicView

app_name = 'campaing-app'
# TODO: complete campaing HERE
urlpatterns = [
    path('campaing', Campaings.as_view({
        'get': 'list',
        'post': 'create'}), name='campaing'),
    # path('campaingsl', Campaings.as_view(), name='campaing'),

    # path('campaing/<int:pk>', CampaingView.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'delete': 'delete',
    #     'patch': 'patch'}), name='detail-campaing'),
    # path('campaings', CampaingPublicView.as_view({
    #     'get': 'list'}), name='public-campaing')
]
