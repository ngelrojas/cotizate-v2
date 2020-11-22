from core.queries.campaingQuery import CampaingHeaderQuery as CampHQ
from core.queries.campaingBodyQuery import CampaingBodyQuery as CampBQ
from core.queries.profilesQuery import ProfileQueryCompany
from core.queries.currencyQuery import CurrencyQuery
from core.profile import PersonalProfile
from core.profileCompany import ProfileCompany


class CampHeaderComp:
    """methods components"""

    @classmethod
    def saving_campaing(cls, request):
        """create a campaing"""
        camp_header = CampHQ.get_campch_id(request.data.get("header"))
        current_currency = CurrencyQuery.get_currency(request.data.get("currency"))
        current_profile = PersonalProfile.objects.filter(user=request.user).last()
        current_profile_company = ProfileQueryCompany.get_profile_company(
            current_profile
        )
        resp = CampBQ.save_campaing(
            request,
            camp_header,
            current_currency,
            current_profile,
            current_profile_company,
        )

        return resp

    @classmethod
    def updating_campaing(cls, request, pk):
        """create a campaing"""
        camp_header = CampHQ.get_campch_id(request.data.get("header"))
        current_currency = CurrencyQuery.get_currency(request.data.get("currency"))
        current_profile = PersonalProfile.objects.get(user=request.user)
        current_profile_company = ProfileQueryCompany.get_profile_company(
            current_profile
        )
        resp = CampBQ.update_campaing(
            request,
            camp_header,
            current_currency,
            current_profile,
            current_profile_company,
            pk,
        )

        return resp
