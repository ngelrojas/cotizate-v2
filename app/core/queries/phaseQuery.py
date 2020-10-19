from core.phase import Phase
from core.user import User
from core.campaing import CampaingHeader


class PhaseQuery:
    """phase queries"""

    @staticmethod
    def get_list_phase(header_id):
        """get list all phases about current campaing"""

        return Phase.objects.filter(header=header_id)

    @staticmethod
    def retrieve_phase(pk, header_id):
        """retrieve phase header_id, phase_pk"""
        return Phase.objects.get(id=pk, header=header_id)
