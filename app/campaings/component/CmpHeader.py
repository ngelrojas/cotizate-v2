from core.queries.campaingQuery import CampaingHeaderQuery as CampHQ
from core.queries.campaingBodyQuery import CampaingBodyQuery as CampBQ
from core.queries.currencyQuery import CurrencyQuery


class CampHeaderComp:
    """methods components"""

    @classmethod
    def saving_campaing(cls, request):
        """create a campaing"""
        camp_header = CampHQ.get_campch_id(request.data.get("header"))
        current_currency = CurrencyQuery.get_currency(request.data.get("currency"))
        resp = CampBQ.save_campaing(request, camp_header, current_currency)

        return resp
