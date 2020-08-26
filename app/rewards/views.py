from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializers import RewardSerializer
from core.reward import Reward


class RewardView(viewsets.ViewSet):
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
                request,
                request.data.get('campaing_id'))
            serializer = self.serializer_class(queryset, many=True)
            return Response({'data': serializer.data},
                            status=status.HTTP_200_OK)
        except Reward.DoesNotExist as err:
            return Response({'data': False,
                             'msg': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        """retrieve reward current campaing"""
        try:
            current_reward = Reward.get_reward(self, request, pk)
            serializer = self.serializer_class(current_reward)
            return Response({'data': serializer.data},
                            status=status.HTTP_200_OK)
        except Reward.DoesNotExist as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """create reward"""
        try:
            data = request.data.copy()
            data['users'] = request.user.id
            serializer = self.serializer_class(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'data': True,
                                 'msg': 'reward saved.'},
                                status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'data': False,
                             'msg': f'{err}'},
                            status=status.HTTP_400_BAD_REQUEST)
        return serializer.save(owner=self.request.user)

    def update(self, request, pk):
        """update reward"""
        try:
            current_reward = Reward.get_reward(self, request, pk)
            data_send = {
                'title': request.data.get('title'),
                'description': request.data.get('description'),
                'amount': request.data.get('amount'),
                'campaings': current_reward.id,
                'users': request.user.id}
            serializer = self.serializer_class(current_reward, data=data_send)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'data': serializer.data,
                                 'msg': 'reward updated.'},
                                status=status.HTTP_200_OK)
        except Reward.DoesNotExist as err:
            return Response({'data': False,
                             'msg': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        """delete reward"""
        try:
            Reward.delete_reward(self, request, pk)
            return Response({'data': True,
                             'msg': 'reward deleted.'},
                            status=status.HTTP_204_NO_CONTENT)
        except Reward.DoesNotExist as err:
            return Response({'data': False,
                             'msg': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)
