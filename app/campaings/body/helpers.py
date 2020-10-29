from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.campaing import CampaingBody
from core.queries.campaingBodyQuery import CampaingBodyQuery as CampBQ
from .serializers import CampaingBodySerializer


class HelperBody(viewsets.ModelViewSet):
    """Campaing
    - helper
    """

    serializer_class = CampaingBodySerializer
    permission_classes = (IsAuthenticated,)
    queryset = CampaingBody.objects.all()

    def retrieve(self, request, pk):
        """get last campaing body"""
        try:
            current_campaingh = CampBQ.retrieve_campaing_body(pk)
            serializer = self.serializer_class(current_campaingh)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except CampaingBody.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )
