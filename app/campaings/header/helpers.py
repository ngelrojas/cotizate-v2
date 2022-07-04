from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.campaing import Campaing
from core.queries.campaingQuery import CampaingHeaderQuery as CampHQ
from core.profile import PersonalProfile
from .serializers import CampaingHeaderSerializer
from .serializers import CHDetailSerializer


class HelperHeader(viewsets.ModelViewSet):
    """Campaing
    - helper
    """

    serializer_class = CampaingHeaderSerializer
    queryset = Campaing.objects.all()
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        """get last campaing header"""
        try:
            current_campaingh = CampHQ.get_last_id(request)
            serializer = CHDetailSerializer(current_campaingh)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )
