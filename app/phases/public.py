from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializers import RewardSerializer
from core.reward import Reward


class RewardPublic(viewsets.ViewSet):
    """
    retrieve: get a reward public join with campaing
    """
    serializer_class = RewardSerializer
    queryset = Reward.objects.all()

    def list(self, request):
        """list all rewards public
        """
        try:
            queryset = Reward.get_all_reward_public(
                self,
                request.data.get('campaing_id'))
            serializer = self.serializer_class(queryset, many=True)
            return Response({'data': serializer.data},
                            status=status.HTTP_200_OK)
        except Reward.DoesNotExist as err:
            return Response({'data': False,
                             'msg': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)
