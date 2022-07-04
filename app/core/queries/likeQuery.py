# from django.db.models import Q
from core.like import Like
from core.campaing import Campaing


class LikeQuery:
    """query like"""

    @staticmethod
    def get_all(current_user):
        """get list all about the user like=true"""
        return Like.objects.filter(user=current_user)

    @staticmethod
    def get_retrieve(pk):
        """get list all about the user like=true"""
        try:
            header_pk = Campaing.objects.get(id=pk)
            return Like.objects.get(header=header_pk)
        except:
            return False

    @classmethod
    def saving_likes(cls, request, pk):
        """
        - create like form current user
        return boolean
        """
        try:
            camp = Campaing.objects.get(id=pk)
            liked = Like.objects.create(
                user=request.user, header=camp, liked=request.data.get("liked")
            )
            return liked
        except:
            return False
