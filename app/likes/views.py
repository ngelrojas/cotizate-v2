from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.like import Like
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
            current_like = Like.objects.exclude(liked=False).filter(
                users=request.user.id
            )
            serializer = self.serializer_class(current_like, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def create(self, request):
        """create like to current user and campaing"""
        try:
            data = request.data.copy()
            data["users"] = request.user.id
            serializer = self.serializer_class(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    {"data": True, "msg": "like saved."}, status=status.HTTP_201_CREATED
                )
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk):
        """retrieve like to current user and campaing"""
        try:
            current_like = Like.get_retrieve_like(self, request, pk)
            serializer = self.serializer_class(current_like)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, pk):
        """update like to current user and campaing"""
        try:
            current_like = Like.get_retrieve_like(self, request, pk)
            serializer = self.serializer_class(
                current_like, data=request.data, partial=True
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    {"data": True, "msg": "update like."}, status=status.HTTP_200_OK
                )
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )
