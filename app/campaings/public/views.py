from rest_framework import viewsets
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response
from core.queries.campaingQuery import CampaingPublicQuery
from core.campaing import CampaingBody
from .serializers import CampaingPublicSerializer
from .serializers import CampaingDetailSerializer


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

    # TODO: check in the postman
    def retrieve(self, request, the_slug):
        """retrieve using slug campaing body"""
        try:
            camp_detail = CampaingPublicQuery.detail_campaing(the_slug)
            # camp_detail = CampaingBody.objects.get(slug=the_slug, status=5)
            serializer = CampaingDetailSerializer(camp_detail)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({"data": f"{err}"}, status=status.HTTP_400_BAD_REQUEST)


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
