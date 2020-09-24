from core.phase import Phase


class PhaseQuery:
    """phase queries"""

    @staticmethod
    def get_list_phase(header_id):
        """get list all phases about current campaing"""
        return Phase.objects.filter(header=header_id)

    @staticmethod
    def retrieve_phase(header_id, pk):
        """retrieve phase header_id, phase_pk"""
        return Phase.objects.get(header=header_id, id=pk)
