from django.db.models import Q
from core.campaing import CampaingHeader


class CampaingHeaderQuery:
    """query campaing header"""

    @staticmethod
    def get_list_ch(request):
        """get list campaing header"""
        return CampaingHeader.objects.filter(user=request.user)

    @staticmethod
    def retrieve_ch(request, pk):
        """retrieve current campaing header"""
        return CampaingHeader.objects.get(user=request.user, id=pk)

    @staticmethod
    def get_campch_id(pk):
        """get id campaing header"""
        return CampaingHeader.objects.get(id=pk)

    @staticmethod
    def get_last_id(request):
        """get last campaing header from current user"""
        return CampaingHeader.objects.filter(user=request.user).last()
