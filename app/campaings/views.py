from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.campaing import Campaing
from core.profile import PersonalProfile
from .serializers import CampaingSerializer


class Campaings(viewsets.ViewSet):
    """Campaing
    - list: list campaing to current user
    - create: create campaing to current user
    - retrieve: retrieve campaing to current user and ID campaing
    - update: update campaing to current user and ID campaing
    """
    serializer_class = CampaingSerializer
    queryset = Campaing.objects.all()

    def list(self, request):
        """list all campaings to current user"""
        try:
            list_campaing = Campaing.get_not_del_and_archived(self, request)
            serializer = self.serializer_class(list_campaing, many=True)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        """create campaing to current user"""
        try:
            data = request.data.copy()
            current_profile = PersonalProfile.objects.get(user=request.user)
            if current_profile.complete is not True:
                return Response({'data': False,
                                 'msg': 'profile user is not complete'},
                                status=status.HTTP_200_OK)

            data['users'] = request.user.id
            data['profiles'] = request.user.id
            serializer = self.serializer_class(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'data': True,
                                 'msg': 'campaing is saved.'},
                                status=status.HTTP_201_CREATED)

        except Exception as err:
            return Response({'data': False,
                             'mgs': f'{err}'},
                            status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        """retrieve campaing to current user and ID campaing"""
        try:
            current_campaing = Campaing.retrieve_campaing(self, request.user, pk)
            serializer = self.serializer_class(current_campaing)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'data': False,
                             'msg': f'{err}'},
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        """update current campaing to current user and ID campaing"""
        try:
            current_campaing = Campaing.retrieve_campaing(self, request.user, pk)
            serializer = self.serializer_class(
                current_campaing,
                data=request.data,
                partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'data': True,
                                 'msg': 'campaing updated.'},
                                status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'data': False,
                             'msg': f'{err}'},
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """retrieve campaing to current user and ID campaing"""
        try:
            Campaing.update_to_delete(self, request.user, pk)
            return Response({'data': True,
                             'msg': 'campaing deleted.'},
                            status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'data': False,
                             'msg': f'{err}'},
                            status=status.HTTP_400_BAD_REQUEST)
