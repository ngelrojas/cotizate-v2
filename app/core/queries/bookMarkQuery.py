# from django.db.models import Q
from core.bookMark import BookMark


class BookMarkQuery:
    """query like"""

    @staticmethod
    def get_all(current_user):
        """get list all about the user marked=true"""
        return BookMark.objects.filter(user=current_user, marked=True)

    @staticmethod
    def get_retrieve(request, pid):
        """get list all about the user marked=true"""
        return BookMark.objects.get(user=request.user, id=pid)

    @classmethod
    def saving_bookmark(cls, request, camp_header):
        """save book marked naturally"""
        bookmark = BookMark.objects.create(
            user=request.user,
            header=camp_header,
            marked=request.data.get("marked"),
        )
        return bookmark
