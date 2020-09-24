from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.improve import Improve
from core.queries.improveQuery import ImproveQuery
from .serializers import ImproveSerializer
from .componentImprove.compImprove import CompImprove


class ImproveView(viewsets.ViewSet):
    """
    list:
        - list all improve
        about the current improve
    """

    serializer_class = ImproveSerializer
    queryset = Improve.objects.all()

    def list(self, request):
        """
        list all improve
        about the current campaing
        """
        try:
            current_list_improve = ImproveQuery.get_list_improve(
                request.data.get("header_id")
            )
            serializer = self.serializer_class(current_list_improve, many=True)
            return Response(
                {"data": serializer.data, "msg": "ok"}, status=status.HTTP_200_OK
            )
        except Improve.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )

    def retrieve(self, request, pk):
        """retrieve improve current campaing_header_id, campaing_id"""
        try:
            current_improve = ImproveQuery.retrieve_improve(
                request.data.get("header_id"), pk
            )
            serializer = self.serializer_class(current_improve)
            return Response(
                {"data": serializer.data, "msg": "ok"}, status=status.HTTP_200_OK
            )
        except Improve.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )

    def create(self, request):
        """create improve"""
        try:
            datas = CompImprove.save_array_data(request, self.serializer_class)
            return Response(
                {"data": datas, "msg": "improve saved."},
                status=status.HTTP_201_CREATED,
            )
        except Improve.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )

    def update(self, request, pk):
        """update improve"""
        try:
            current_improve = ImproveQuery.retrieve_improve(
                request.data.get("header_id"), pk
            )
            serializer = self.serializer_class(current_improve, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    {"data": True, "msg": "improve data updated."},
                    status=status.HTTP_200_OK,
                )
        except Improve.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, pk):
        """delete improve"""
        try:

            current_improve = ImproveQuery.retrieve_improve(
                request.data.get("header_id"), pk
            )

            current_improve.delete()
            return Response(
                {"data": True, "msg": " improve deleted."},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Improve.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )
