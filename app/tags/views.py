from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializers import TagSerializer
from core.tag import Tag


class TagView(viewsets.ModelViewSet):
    """
    list
        - list all tags
    retrieve
        - get a tags
    """

    serializer_class = TagSerializer
    queryset = Tag.objects.all()

    def list(self, request, campId):
        """
        list tags about campaing
        """
        try:
            list_tags = Tag.objects.filter(campaings=campId)
            serializer = self.serializer_class(list_tags, many=True)

            return Response({"data": serializer.data}, status=status.HTTP_200_OK)

        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )

    def create(self, request):
        """
        create tag about campaing
        """
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"data": "tag saved."}, status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )
