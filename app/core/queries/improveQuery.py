from core.improve import Improve


class ImproveQuery:
    """improve query"""

    @staticmethod
    def get_list_improve(header_id):
        """get list improve about campaing"""
        return Improve.objects.filter(header=header_id)

    @staticmethod
    def retrieve_improve(header_id, pk):
        """retrieve improve about campaing"""
        return Improve.objects.get(header=header_id, id=pk)
