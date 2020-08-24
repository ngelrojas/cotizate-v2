from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.campaing import Campaing
from .serializers import CampaingSerializer
# from .serializers import CCampaingSerializer
# from api.cotizate import ActiveUser, ProfileComplete
from core.profile import PersonalProfile
# from core.profile import CompanyProfile


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
            list_campaing = Campaing.objects.filter(users=request.user)
            serializer = self.serializer_class(list_campaing, many=True)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_400_BAD_REQUEST)

    # TODO: complete Campaing HERE
    def create(self, request):
        """create campaing to current user"""
        try:
            # get current profile
            data = request.data.copy()
            current_profile = PersonalProfile.objects.get(user=request.user)
            if current_profile.complete is not True:
                return Response({'data': 'profile user is not complete'}, status=status.HTTP_200_OK)

            data['users'] = request.user.id
            data['profiles'] = request.user.id
            serializer = self.serializer_class(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'data': 'campaing is saved.'}, status=status.HTTP_201_CREATED)

        except Exception as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_400_BAD_REQUEST)
