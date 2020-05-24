from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.profile import PersonalProfile as PerPF
from .personalSerializers import PersonalSerializer
from api.cotizate import ProfileComplete


class UpdatePersonalView(viewsets.ModelViewSet):
    """update profile current user"""
    serializer_class = PersonalSerializer
    queryset = PerPF.objects.all()

    def retrieve(self, request, pk=None):
        """retrieve profile current user"""
        try:
            prof = ProfileComplete()
            current_profile = prof.currentProfile(
                PerPF, request)
            serializer = self.serializer_class(current_profile)
            return Response({'data': serializer.data},
                            status=status.HTTP_200_OK)
        except PerPF.DoesNotExist as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        """update profile current user"""
        prof = ProfileComplete()
        current_profile = prof.currentProfile(
            PerPF, request)
        serializer = self.serializer_class(
            current_profile,
            data=request.data,
            partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            pro_complete = ProfileComplete()
            complete = pro_complete.update_profile(
                PerPF,
                request)
            return Response({'data': 'profile updated.',
                             'complete': complete},
                            status=status.HTTP_200_OK)
        return Response({'error': 'something wrong happend'},
                        status=status.HTTP_400_BAD_REQUEST)
