from datetime import datetime
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.campaing import CampaingBody
from core.queries.campaingBodyQuery import CampaingBodyQuery as CampBQ
from .serializers import CampaingBodySerializer


class CampaingsBody(viewsets.ModelViewSet):
    """Campaing
    - list: list campaing to current user
    - create: create campaing to current user
    - retrieve: retrieve campaing to current user and ID campaing
    - update: update campaing to current user and ID campaing
    """

    serializer_class = CampaingBodySerializer
    queryset = CampaingBody.objects.all()

    def create(self, request):
        """create campaing body current user"""
        try:
            public_camp = datetime.strptime(
                request.data.get("public_at"), "%d/%m/%Y"
            ).strftime("%Y-%m-%dT%H:%M:%S-00:00")
            send_data = {
                "title": request.data.get("title"),
                "video_main": request.data.get("video_main"),
                "imagen_main": request.data.get("imagen_main"),
                "excerpt": request.data.get("excerpt"),
                "description": request.data.get("description"),
                "public_at": public_camp,
                "header": request.data.get("header"),
                "currency": 1,
                "short_url": request.data.get("short_url"),
                "slogan_campaing": request.data.get("slogan_campaing"),
            }

            serializer = self.serializer_class(data=send_data)
            if serializer.is_valid(raise_exception=True):
                camp_cb = serializer.save()
                return Response(
                    {"data": camp_cb.id, "msg": "campaing body is saved."},
                    status=status.HTTP_201_CREATED,
                )

        except CampaingBody.DoesNotExist as err:
            return Response(
                {"data": False, "mgs": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk):
        """retrieve campaing body using header_id and pk=campaing_body"""
        try:
            current_campaing = CampBQ.retrieve_cb(request.data.get("header_id"), pk)
            serializer = self.serializer_class(current_campaing)
            return Response(
                {"data": serializer.data, "msg": "ok"}, status=status.HTTP_200_OK
            )

        except CampaingBody.DoesNotExist as err:
            return Response(
                {"data": False, "mgs": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, pk):
        """update campaing body using header_id and pk=campaing_body"""
        try:
            current_campaing = CampBQ.retrieve_cb(request.data.get("header_id"), pk)
            serializer = self.serializer_class(
                current_campaing, data=request.data, partial=True
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    {"data": True, "msg": "campaing body updated."},
                    status=status.HTTP_200_OK,
                )
        except CampaingBody.DoesNotExist as err:
            return Response(
                {"data": False, "mgs": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk):
        """retrieve campaing to current user and ID campaing"""
        try:
            CampBQ.delete_cb(request.data.get("header_id"), pk)
            return Response(
                {"data": True, "msg": "campaing deleted."},
                status=status.HTTP_204_NOT_CONTENT,
            )
        except CampaingBody.DoesNotExist as err:
            return Response(
                {"data": False, "mgs": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )
