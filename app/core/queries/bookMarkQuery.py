# from django.db.models import Q
from core.bookMark import BookMark
from core.campaing import Campaing


class BookMarkQuery:
    """query like"""

    @staticmethod
    def get_all(current_user):
        """get list all about the user marked=true"""
        return BookMark.objects.filter(user=current_user, marked=True)

    @staticmethod
    def get_retrieve(pid):
        """get list all about the user marked=true"""
        try:
            return BookMark.objects.get(header=pid)
        except:
            return False

    @classmethod
    def saving_bookmark(cls, request, pk):
        """save book marked naturally"""
        try:
            header = Campaing.objects.get(id=pk)
            bookmark = BookMark.objects.create(
                user=request.user,
                header=header,
                marked=request.data.get("marked"),
            )
            return bookmark
        except:
            return False
