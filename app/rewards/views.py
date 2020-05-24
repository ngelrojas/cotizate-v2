from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializers import RewardSerializer
from core.reward import Reward


class RewardView(viewsets.ModelViewSet):
    """
        list:
            - list all rewards
            about the current campaing
    """
    serializer_class = RewardSerializer
    queryset = Reward.objects.all()

    def list(self, request):
        """list all rewards
        about the current campaing
        """
        try:
            queryset = Reward.get_all_reward(
                self,
                request.data.get('campaing_id'))
            serializer = self.serializer_class(queryset, many=True)
            return Response({'data': serializer.data},
                            status=status.HTTP_200_OK)
        except Reward.DoesNotExist as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        """retrieve reward current campaing"""
        try:
            current_reward = Reward.get_reward(self, pk)
            serializer = self.serializer_class(current_reward)
            return Response({'data': serializer.data},
                            status=status.HTTP_200_OK)
        except Reward.DoesNotExist as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)

    def perform_create(self, serializer):
        """create reward"""
        return serializer.save()

    def update(self, request, pk=None):
        """update reward"""
        try:
            current_reward = Reward.get_reward(self, pk)
            data_send = {
                'title': request.data.get('title'),
                'description': request.data.get('description'),
                'amount': request.data.get('amount'),
                'campaings': current_reward.id,
                'users': request.data.get('users')}
            serializer = self.serializer_class(current_reward, data=data_send)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'data': serializer.data},
                                status=status.HTTP_200_OK)
        except Reward.DoesNotExist as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        """delete reward"""
        try:
            Reward.delete_reward(self, pk)
            return Response({'data': 'reward deleted'},
                            status=status.HTTP_204_NO_CONTENT)
        except Reward.DoesNotExist as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)
