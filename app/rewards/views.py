from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.campaing import Campaing
from core.reward import Reward
from core.phase import Phase
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
            list_reward = Reward.get_all(request, pk)
            serializer = self.serializer_class(list_reward, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def create(self, request):
        """create reward"""
        try:
            obj_campaing = Campaing.get_campaing_id(request, request.data.get('campaing_id'))
            obj_phase = Phase.get_phase(obj_campaing, request.data.get('phase_id'))
            resp = Reward.created(request, obj_campaing, obj_phase)
            return Response(
                    {"data": resp, "msg":"reward created."},
                    status=status.HTTP_201_CREATED,
            )
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, pk):
        """update reward"""
        try:
            current_reward = Reward.updated(request, pk)
            # serializer = self.serializer_class(current_reward, data=request.data)
            # if serializer.is_valid(raise_exception=True):
            #     serializer.save()
            return Response(
                    {"data": current_reward, "msg": "reward updated."},
                status=status.HTTP_200_OK,
            )
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk):
        """delete reward"""
        try:
            dele = Reward.erase(request, pk)
            return Response(
                {"data": dele, "msg": "reward deleted."},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
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
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )
