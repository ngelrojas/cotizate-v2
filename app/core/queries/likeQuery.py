# from django.db.models import Q
from core.like import Like


class LikeQuery:
    """query like"""

    @staticmethod
    def get_all(current_user):
        """get list all about the user like=true"""
        return Like.objects.filter(user=current_user)

    @staticmethod
    def get_retrieve(pk):
        """get list all about the user like=true"""
        return Like.objects.get(header=pk)

    @classmethod
    def saving_likes(cls, request, camp_header):
        """save like naturally"""
        like = Like.objects.create(
            user=request.user,
            header=camp_header,
            liked=request.data.get("liked"),
        )
        return like
