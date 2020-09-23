from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.reward import Reward
from core.queries.rewardQuery import RewardQuery
from .serializers import RewardSerializer


class RewardView(viewsets.ViewSet):
    """
    list:
        - list all rewards
        about the current campaing
    """

    serializer_class = RewardSerializer
    queryset = Reward.objects.all()

    def list(self, request):
        """
        list all rewards
        about the current campaing
        """
        try:
            current_list_reward = RewardQuery.get_list_reward(
                request.data.get("header_id")
            )
            serializer = self.serializer_class(current_list_reward, many=True)
            return Response(
                {"data": serializer.data, "msg": "ok"}, status=status.HTTP_200_OK
            )
        except Reward.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )

    def retrieve(self, request, pk):
        """retrieve reward current campaing_header_id, campaing_id"""
        try:
            current_reward = RewardQuery.retrieve_reward(
                request.data.get("header_id"), pk
            )
            serializer = self.serializer_class(current_reward)
            return Response(
                {"data": serializer.data, "msg": "ok"}, status=status.HTTP_200_OK
            )
        except Reward.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )

    # TODO: this method recived an array object and need looping
    def create(self, request):
        """create reward"""
        try:
            # for data in request.data:
            data = request.data.copy()
            data["user"] = request.user
            serializer = self.serializer_class(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    {"data": True, "msg": "reward saved."}, status=status.HTTP_200_OK
                )
        except Reward.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )

    def update(self, request, pk):
        """update reward"""
        try:
            current_reward = Reward.get_reward(self, request, pk)
            data_send = {
                "title": request.data.get("title"),
                "description": request.data.get("description"),
                "amount": request.data.get("amount"),
                "campaings": current_reward.id,
                "users": request.user.id,
            }
            serializer = self.serializer_class(current_reward, data=data_send)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    {"data": serializer.data, "msg": "reward updated."},
                    status=status.HTTP_200_OK,
                )
        except Reward.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, pk):
        """delete reward"""
        try:
            Reward.delete_reward(self, request, pk)
            return Response(
                {"data": True, "msg": "reward deleted."},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Reward.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )
