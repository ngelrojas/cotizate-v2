from rest_framework import viewsets
from rest_framework import filters
from core.campaing import Campaing
from .serializers import CampaingPublicSerializer


class CampaingPublic(viewsets.ModelViewSet):
    """
    show all campaing public
    """
    serializer_class = CampaingPublicSerializer
    queryset = Campaing.get_all_available()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', ]


class CampaingCompleted(viewsets.ModelViewSet):
    """
    show all campaing public completed
    """
    serializer_class = CampaingPublicSerializer
    queryset = Campaing.get_completed_campaings()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', ]


class CampaingTerminated(viewsets.ModelViewSet):
    """
    show all campaing public terminated
    """
    serializer_class = CampaingPublicSerializer
    queryset = Campaing.get_terminated_campaings()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', ]
