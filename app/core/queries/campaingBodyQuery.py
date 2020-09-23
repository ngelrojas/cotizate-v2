from django.db.models import Q
from core.campaing import CampaingBody


class CampaingBodyQuery:
    """query campaing body"""

    @staticmethod
    def get_list_cb(data_list):
        """
        get list campaing body
        get all campaing without deleted and archived
        for current campaing header
        """
        return CampaingBody.objects.filter(header=data_list).exclude(
            Q(status=8) | Q(status=9)
        )

    @staticmethod
    def retrieve_cb(header_id, pk):
        """retrieve current campaing body"""
        return CampaingBody.objects.get(id=pk, header=header_id)

    @staticmethod
    def delete_cb(header_id, pk):
        """update status to deleted=9"""
        camp = CampaingBody.objects.exclude(
            Q(status=5) | Q(status=6) | Q(status=7) | Q(status=8)
        ).get(header=header_id, id=pk)
        camp.status = 9
        camp.save()
        return camp
