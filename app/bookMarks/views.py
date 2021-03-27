from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.bookMark import BookMark
from core.campaing import CampaingHeader
from core.queries.bookMarkQuery import BookMarkQuery
from .serializers import BookMarkSerializer


class BookMarkView(viewsets.ModelViewSet):
    """BookMark
    - list: list likes to current user
    - create: create likes to current user
    - retrieve: retrieve like to current user and ID campaing
    - update: update like to current user and ID campaing
    """

    serializer_class = BookMarkSerializer
    queryset = BookMark.objects.all()

    def list(self, request):
        """list all bookmark about current user"""
        try:
            current_like = BookMarkQuery.get_all(request.user)
            serializer = self.serializer_class(current_like, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def create(self, request):
        """create like to current user and campaing"""
        try:
            camp_header = CampaingHeader.objects.get(id=request.data.get("header"))
            BookMarkQuery.saving_bookmark(request, camp_header)
            return Response(
                {"data": "book mark created."}, status=status.HTTP_201_CREATED
            )
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk):
        """retrieve bookmarked to current user and campaing"""
        try:
            current_like = BookMarkQuery.get_retrieve(pk)
            serializer = self.serializer_class(current_like)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, pk):
        """update like to current user and campaing"""
        try:
            current_marked = BookMarkQuery.get_retrieve(pk)
            if current_marked:
                serializer = self.serializer_class(
                    current_marked, data=request.data, partial=True
                )
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(
                        {"data": "update book marked."}, status=status.HTTP_200_OK
                    )
            marked = BookMarkQuery.saving_bookmark(request, pk)
            if marked:
                return Response(
                    {"data": True, "msg": "marked created."},
                    status=status.HTTP_201_CREATED,
                )
            return Response(
                {"data": False, "msg": "campaing not exists."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )
