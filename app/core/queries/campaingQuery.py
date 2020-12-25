from django.db.models import Q
from core.campaing import CampaingHeader
from core.campaing import CampaingBody
from core.user import User
from core.profile import PersonalProfile


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


class CampaingPublicQuery:
    """campaing query public"""

    @staticmethod
    def get_list_cp(status_campaing):
        """get list public campaings using status"""
        status_public = 5
        return CampaingBody.objects.filter(
            status=status_public, flag=status_campaing
        ).order_by("-id")

    @staticmethod
    def detail_campaing(the_slug):
        """rules:
        - searching campaing using slug
        - camaping is public
        """
        status_camp_public = 5
        return CampaingBody.objects.get(slug=the_slug, status=status_camp_public)


class CampaingPrivateQuery:
    """campaing private query"""

    @staticmethod
    def get_list_camp_header(request):
        current_header = CampaingHeader.objects.filter(user=request.user)
        return current_header

    @staticmethod
    def list_camps(list_header, pk):
        list_camp = []
        try:
            for header_camp in list_header:
                list_camp.append(
                    CampaingBody.objects.get(header=header_camp, status=pk)
                )
            return list_camp
        except:
            return list_camp
