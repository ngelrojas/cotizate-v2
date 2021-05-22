from django.core.files.storage import FileSystemStorage
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.denounce import DenouncePublic
from .serializers import DenouncePublicSerializer


class DenouncePublicView(viewsets.ModelViewSet):
    """
    retrieve
        - get all  denounce public
    """

    serializer_class = DenouncePublicSerializer
    queryset = DenouncePublic.objects.all()

    def retrieve(self, request, pk):
        """
        pk = denounce public id
        """
        try:
            denounce_retrieve = DenouncePublic.objects.get(id=pk)
            serializer = self.serializer_class(denounce_retrieve)

            return Response({"data": serializer.data}, status=status.HTTP_200_OK)

        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )

    def create(self, request):
        """
        denounce public create
        """
        try:
            data = request.data
            serializer = self.serializer_class(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    {"data": True, "msg": "denounce public created"},
                    status=status.HTTP_201_CREATED,
                )
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )
