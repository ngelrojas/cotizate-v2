from django.core.files.storage import FileSystemStorage
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializers import UploadSerializer
from core.upload import Upload
from .helpers.Tools import Tools


class UploadView(viewsets.ModelViewSet):
    """
    retrieve
        - get a upload images
    """

    serializer_class = UploadSerializer
    queryset = Upload.objects.all()

    def retrieve(self, request, campId):
        """
        list tags about campaing
        """
        try:
            list_img = Upload.objects.filter(campaings=campId)
            serializer = self.serializer_class(list_img, many=True)

            return Response({"data": serializer.data}, status=status.HTTP_200_OK)

        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )

    def create(self, request):
        """
        upload images
        """
        try:
            image_file = request.FILES["image_file"]
            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            image_url = fs.url(filename)
            tools = Tools()
            resp = tools.saving_images(request, image_url)
            return Response({"data": f"{resp}"}, status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )
