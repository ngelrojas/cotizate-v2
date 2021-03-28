from django.core.files.storage import FileSystemStorage
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializers import UpdatingSerializer
from core.updating import Updating
from core.campaing import CampaingHeader


class UpdatingView(viewsets.ModelViewSet):
    """
    retrieve
        - get all updateing
    """

    serializer_class = UpdatingSerializer
    queryset = Updating.objects.all()

    def retrieve(self, request, pk):
        """
        list tags about campaing
        """
        try:
            camp_id = CampaingHeader.objects.get(id=pk)
            list_updating = Updating.objects.get(header=camp_id)
            serializer = self.serializer_class(list_updating, many=True)

            return Response({"data": serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"data": False, "msg": f"{e}"}, status=status.HTTP_404_NOT_FOUND
            )

    def create(self, request):
        """
        create updating for each project
        """
        try:
            serializer = self.serializer_class(request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    {"data": True, "msg": "updating created."},
                    status=status.HTTP_201_CREATED,
                )
        except Exception as e:
            return Response(
                {"data": False, "msg": f"{e}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, pk):
        """updating project"""
        try:
            updating_u = Updating.objects.get(header=pk, id=request.data.get("id"))
            serializer = self.serializer_class(updating_u, data=request.data, many=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    {"data": True, "msg": "updating project"}, status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response(
                {"data": False, "msg": f"{e}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk):
        """delete updateings project"""
        try:
            updating_u = Updating.objects.get(header=pk, id=request.data.get("id"))
            updating_u.delete()
            return Response(
                {"data": True, "msg": "delete updating project"},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Exception as e:
            return Response(
                {"data": False, "msg": f"{e}"}, status=status.HTTP_400_BAD_REQUEST
            )
