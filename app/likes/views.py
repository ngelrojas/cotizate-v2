from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.like import Like
from core.campaing import CampaingHeader
from core.queries.likeQuery import LikeQuery
from .serializers import LikeSerializer


class LikeView(viewsets.ModelViewSet):
    """Like
    - list: list likes to current user
    - create: create likes to current user
    - retrieve: retrieve like to current user and ID campaing
    - update: update like to current user and ID campaing
    """

    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def list(self, request):
        """list all like about current user"""
        try:
            current_like = LikeQuery.get_all(request.user)
            serializer = self.serializer_class(current_like, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def create(self, request):
        """create like to current user and campaing"""
        try:
            camp_header = CampaingHeader.objects.get(id=request.data.get("header"))
            LikeQuery.saving_likes(request, camp_header)
            return Response({"data": "like created."}, status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk):
        """retrieve like to current user and campaing"""
        try:
            current_like = LikeQuery.get_retrieve(pk)
            serializer = self.serializer_class(current_like)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, pk):
        """
        update like to current user and campaing
        pk = header campaing
        """
        try:
            current_like = LikeQuery.get_retrieve(pk)
            if current_like:
                serializer = self.serializer_class(
                    current_like, data=request.data, partial=True
                )
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response({"data": "update like."}, status=status.HTTP_200_OK)
            liked = LikeQuery.create_likes(request, pk)
            if liked:
                return Response(
                    {"data": True, "msg": "create like."},
                    status=status.HTTP_201_CREATED,
                )
            return Response(
                {"data": False, "msg": "campaing not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
