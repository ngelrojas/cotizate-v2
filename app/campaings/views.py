from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.campaing import Campaing
from .serializers import CampaingSerializer
from .serializers import CCampaingSerializer
from api.cotizate import ActiveUser, ProfileComplete
from core.profile import PersonalProfile
from core.profile import CompanyProfile


class CampaingView(viewsets.ModelViewSet):
    """
    list all campaing about current user
    TODO: refactor methods to repeat and create
    another layer to consult method, this file is
    just to call request and send response no more
    """
    serializer_class = CCampaingSerializer
    queryset = Campaing.objects.all()

    def list(self, request):
        queryset = Campaing.get_not_del_and_archived(self)
        serializer = CampaingSerializer(queryset, many=True)
        return Response(
            {'data': serializer.data},
            status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """get a campaing in the current user"""
        try:
            active = ActiveUser()
            current_user = active.currentUser(request)
            current_camp = Campaing.retrieve_campaing(self, current_user, pk)
            serializer = CampaingSerializer(current_camp)
            return Response(
                {'data': serializer.data},
                status=status.HTTP_200_OK)
        except Campaing.DoesNotExist as err:
            return Response(
                {'error': f'{err}'},
                status=status.HTTP_404_NOT_FOUND)

    def perform_create(self, serializer):
        """
        create campaing using rules
        the first rule is current user
        complete your profile
        """
        profile = ProfileComplete()
        is_pprofile = profile.isComplete(
            PersonalProfile,
            self.request
        )
        # company profile complete is
        is_cprofile = profile.isComplete(
            CompanyProfile,
            self.request
        )

        if is_pprofile or is_cprofile:
            serializer.save(users=self.request.user)
            return Response(
                {'data': 'campaing created.'},
                status=status.HTTP_201_CREATED)

        return Response(
            {'error': 'current profile is not completed'},
            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        rules to udpate
        - user profile is complete or
          company profile is completed
        - the current campaing is not status 8 or 9
        """
        try:
            profile = ProfileComplete()
            is_pprofile = profile.isComplete(
                PersonalProfile,
                self.request
            )
            # company profile complete is
            is_cprofile = profile.isComplete(
                CompanyProfile,
                self.request
            )

            if is_pprofile or is_cprofile:
                active = ActiveUser()
                current_user = active.currentUser(request)
                current_campaing = Campaing.retrieve_campaing(
                    self, current_user, pk)
                serializer = self.serializer_class(
                    current_campaing,
                    data=request.data,
                    partial=True)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(
                        {'data': 'campaping updated.'},
                        status=status.HTTP_200_OK)
            return Response(
                {'error': 'something wrong'},
                status=status.HTTP_400_BAD_REQUEST)
        except Campaing.DoesNotExist as err:
            return Response(
                {'error': f'{err}'},
                status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        """delete campaing using rules
        - current campaing is not public
        - current campaing is not completed
        - current campaing is not terminated
        """
        try:
            profile = ProfileComplete()
            is_pprofile = profile.isComplete(
                PersonalProfile,
                self.request
            )
            # company profile complete is
            is_cprofile = profile.isComplete(
                CompanyProfile,
                self.request
            )

            if is_pprofile or is_cprofile:
                active = ActiveUser()
                current_user = active.currentUser(request)
                Campaing.update_to_delete(
                    self, current_user, pk)
                return Response(
                    {'data': 'campaing deleted.'},
                    status=status.HTTP_204_NO_CONTENT)

            return Response(
                {'error': 'your profile is not completed'},
                status=status.HTTP_400_BAD_REQUEST)
        except Campaing.DoesNotExist as err:
            return Response(
                {'error': f'{err}'},
                status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk=None):
        """archived campaing using rules
        - current campaing is not public
        - current campaing is not completed
        - current campaing is not terminated
        """
        try:
            profile = ProfileComplete()
            is_pprofile = profile.isComplete(
                PersonalProfile,
                self.request
            )
            # company profile complete is
            is_cprofile = profile.isComplete(
                CompanyProfile,
                self.request
            )

            if is_pprofile or is_cprofile:
                active = ActiveUser()
                current_user = active.currentUser(request)
                Campaing.update_to_archived(self, current_user, pk)
                return Response(
                    {'data': 'campaing is archived.'},
                    status=status.HTTP_200_OK)

            return Response(
                {'error': 'your profile is not completed'},
                status=status.HTTP_400_BAD_REQUEST)
        except Campaing.DoesNotExist as err:
            return Response(
                {'error': f'{err}'},
                status=status.HTTP_404_NOT_FOUND)
