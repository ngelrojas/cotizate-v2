from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.follower import Follower
from .serializers import FollowerSerializer


class FollowerView(viewsets.ModelViewSet):
    """Follower"""

    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()

    def create(self, request):
        """create follower from current user"""
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    {"data": True, "msg": "following"}, status=status.HTTP_201_CREATED
                )
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk):
        """
        following = pk
        - following is id current user
        """
        try:
            current_follow = Follower.objects.get(following=pk)
            serializer = self.serializer_class(current_follow)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, pk):
        """
        follower = current user
        following = campaing user
        status = True or False
        """
        try:
            current_follow = Follower.objects.get(
                following=pk, follower=request.data.get("follower")
            )
            serializer = self.serializer_class(
                current_follow, data=request.data, partial=True
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"data": True}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )
