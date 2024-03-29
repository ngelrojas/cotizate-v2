from django.db.models import Q
from core.campaing import CampaingBody
from core.campaing import CampaingHeader


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
        # current_header = CampaingHeader.objects.get(id=header_id)
        return CampaingBody.objects.get(id=pk, header=header_id)

    @staticmethod
    def delete_cb(pk, header_id):
        """update status to deleted=9"""
        try:
            camp = CampaingBody.objects.get(id=pk, header=header_id)
            camp.status = 9
            camp.save()
            return True
        except Exception:
            return False

    @classmethod
    def save_campaing(
        cls,
        request,
        camp_header,
        current_currency,
        current_profile,
        current_profile_company,
    ):
        try:

            resp = CampaingBody.objects.create(
                title=request.data.get("title"),
                video_main=request.data.get("video_main"),
                imagen_main=request.data.get("imagen_main"),
                excerpt=request.data.get("excerpt"),
                description=request.data.get("description"),
                public_at=request.data.get("public_at"),
                header=camp_header,
                profile=current_profile,
                currency=current_currency,
                short_url=request.data.get("short_url"),
                slogan_campaing=request.data.get("slogan_campaing"),
                profile_ca=current_profile_company,
            )
            return resp
        except Exception as err:
            return err

    @classmethod
    def update_campaing(
        cls,
        request,
        camp_header,
        current_currency,
        current_profile,
        current_profile_company,
        pk,
    ):
        """pk=campaing body ID"""
        camp = CampaingBody.objects.get(id=pk)
        camp.title = request.data.get("title")
        camp.video_main = request.data.get("video_main")
        if request.FILES:
            camp.imagen_main = request.FILES["imagen_main"]
        camp.excerpt = request.data.get("excerpt")
        camp.description = request.data.get("description")
        camp.public_at = request.data.get("public_at")
        camp.header = camp_header
        camp.profile = current_profile
        camp.currency = current_currency
        camp.short_url = request.data.get("short_url")
        camp.slogan_campaing = request.data.get("slogan_campaing")
        if current_profile_company:
            camp.profile_ca = current_profile_company
        camp.save()
        return camp

    @staticmethod
    def retrieve_campaing_body(camp_header_id):
        """return campaing body"""
        return CampaingBody.objects.get(header=camp_header_id)
