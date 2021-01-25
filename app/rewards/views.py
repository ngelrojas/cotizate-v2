from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.campaing import CampaingHeader
from core.reward import Reward
from core.queries.rewardQuery import RewardQuery
from .serializers import RewardSerializer

# from .componentReward.compReward import CompReward


class RewardView(viewsets.ViewSet):
    """
    list:
        - list all rewards
        about the current campaing
    """

    serializer_class = RewardSerializer
    queryset = Reward.objects.all()

    def retrieve(self, request, pk):
        """retrieve reward current campaing_header_id, campaing_id"""
        try:
            reward_header = CampaingHeader.objects.get(id=pk)
            list_reward = Reward.objects.filter(header=reward_header)
            serializer = self.serializer_class(list_reward, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )

    def create(self, request):
        """create reward"""
        try:
            RewardQuery.saving_rewards(request)
            return Response(
                {"data": "reward created."},
                status=status.HTTP_201_CREATED,
            )
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )

    def update(self, request, pk):
        """update reward"""
        try:
            # current_reward = RewardQuery.retrieve_reward(pk, request.data.get("header"))
            current_reward = Reward.objects.get(id=pk, header=request.data.get("header"))
            serializer = self.serializer_class(current_reward, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    {"data": "reward updated."},
                    status=status.HTTP_200_OK,
                )
        except Reward.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, pk):
        """delete reward"""
        try:
            current_reward = Reward.objects.get(id=pk)
            current_reward.delete()
            return Response(
                {"data": True, "msg": "reward deleted."},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Reward.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )


class RewardrView(viewsets.ViewSet):
    """
    retrieve:
        - list all rewards
        about the current campaing
    """

    serializer_class = RewardSerializer
    queryset = Reward.objects.all()

    def retrieve(self, request, pk):
        """
        retrieve reward
        - headerId = pk
        """
        try:
            # reward_header = CampaingHeader.objects.get(id=pk)
            list_reward = Reward.objects.get(id=pk)
            serializer = self.serializer_class(list_reward)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )
