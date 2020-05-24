from rest_framework import viewsets
from rest_framework import filters
from core.campaing import Campaing
from .serializers import CampaingSerializer


class CampaingPublicView(viewsets.ModelViewSet):
    """
    show all campaing public
    """
    serializer_class = CampaingSerializer
    queryset = Campaing.get_all_available()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', ]
