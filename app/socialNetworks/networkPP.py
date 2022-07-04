from rest_framework import viewsets
from rest_framework import filters, status
from rest_framework.response import Response
from core.socialNetwork import SocialNetworkPP
from .serializers import SocialPPSerializer


class SnetWPPView(viewsets.ModelViewSet):
    """
    list
        - list all social network personal profile
    retrieve
        - get a personal profile
    """

    serializer_class = SocialPPSerializer
    queryset = SocialNetworkPP.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "name",
    ]

    def list(self, request):
        """list all about social network pp"""
        try:
            current_pp = request.data.get("current_pp")
            list_networpp = SocialNetworkPP.objects.filter(snet=current_pp)
            serializer = self.serializer_class(list_networpp, many=True)
            return Response(
                {"data": serializer.data, "msg": "list social network."},
                status=status.HTTP_200_OK,
            )
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def create(self, request):
        """create social network"""
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    {"data": True, "msg": "social network personal profile created."},
                    status=status.HTTP_201_CREATED,
                )
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk):
        """retrieve social network current user """
        try:
            current_snpp = SocialNetworkPP.objects.get(snet=pk)
            serializer = self.serializer_class(current_snpp)
            return Response(
                {"data": serializer.data, "msg": "data successfully"},
                status=status.HTTP_200_OK,
            )
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, pk):
        """delete current social network"""
        try:
            current_snt = SocialNetworkPP.objects.get(id=pk)
            current_snt.delete()
            return Response(
                {"data": True, "msg": "personal social network deleted."},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )
