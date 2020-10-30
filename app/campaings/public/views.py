from rest_framework import viewsets
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response
from core.queries.campaingQuery import CampaingPublicQuery
from .serializers import CampaingPublicSerializer


class CampaingPublic(viewsets.ModelViewSet):
    """
    show all campaing public
    """

    serializer_class = CampaingPublicSerializer
    queryset = ""
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "title",
    ]

    def list(self, request, pk):
        """list all campaings"""
        camp_public = CampaingPublicQuery.get_list_cp(pk)
        serializer = self.serializer_class(camp_public, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)


# class CampaingCompleted(viewsets.ModelViewSet):
#     """
#     show all campaing public completed
#     """
#     serializer_class = CampaingPublicSerializer
#     queryset = Campaing.get_completed_campaings()
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['title', ]


# class CampaingTerminated(viewsets.ModelViewSet):
#     """
#     show all campaing public terminated
#     """
#     serializer_class = CampaingPublicSerializer
#     queryset = Campaing.get_terminated_campaings()
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['title', ]
