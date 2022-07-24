from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.bookMark import BookMark
from core.campaing import Campaing
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
            current_like = BookMarkQuery.list_bookmark(request)
            serializer = self.serializer_class(current_like, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk):
        """retrieve bookmarked to current user and campaing"""
        try:
            current_like = BookMarkQuery.get_bookmark(request, pk)
            serializer = self.serializer_class(current_like)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def create(self, request):
        """create like to current user and campaing"""
        try:
            pk = request.data.get("campaing_id")
            campaing = Campaing.get_campaing_id(request, pk)
            created = BookMark.created(request, campaing)
            if created:
                return Response(
                        {"data": created, "msg": "book mark created"},
                        status=status.HTTP_201_CREATED
                )
            return Response(
                {"data": False},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"},
                status=status.HTTP_400_BAD_REQUEST
            )


    def update(self, request, pk):
        """update bookmarked to current user and campaing"""
        try:
            # cp_pk = request.data.get("campaing_id")
            # campaing = Campaing.get_campaing_id(request, cp_pk)
            bookmark = BookMark.updated(request, pk)
            if bookmark:
                return Response(
                        {"data": bookmark, "msg": "bookmark updated"},
                        status=status.HTTP_200_OK
                )
            return Response(
                    {"data": None, "msg": "something error"},
                    status=status.HTTP_404_NOT_FOUND
            )
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
