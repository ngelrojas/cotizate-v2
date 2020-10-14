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
    def retrieve_cb(pk, header_id):
        """retrieve current campaing body"""
        return CampaingBody.objects.get(id=pk, header=header_id)

    @staticmethod
    def delete_cb(pk, header_id):
        """update status to deleted=9"""
        camp = CampaingBody.objects.exclude(
            Q(status=5) | Q(status=6) | Q(status=7) | Q(status=8)
        ).get(id=pk, header=header_id)
        camp.status = 9
        camp.save()
        return camp

    @classmethod
    def save_campaing(cls, request, camp_header, current_currency):
        camp = CampaingBody.objects.create(
            title=request.data.get("title"),
            video_main=request.data.get("video_main"),
            imagen_main=request.FILES.get("imagen_main"),
            excerpt=request.data.get("excerpt"),
            description=request.data.get("description"),
            public_at=request.data.get("public_at"),
            header=camp_header,
            currency=current_currency,
            short_url=request.data.get("short_url"),
            slogan_campaing=request.data.get("slogan_campaing"),
        )
        return camp
