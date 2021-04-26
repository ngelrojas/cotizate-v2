from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializers import DenounceSerializer
from .serializers import DenounceTextSerializer
from core.denounce import Denounce
from core.denounce import DenounceText


class DenounceView(viewsets.ModelViewSet):
    """
    retrieve
        - get all denounces
    """

    serializer_class = DenounceSerializer
    queryset = Denounce.objects.all()

    def list(self, request):
        list_all_denounce = DenounceText.objects.all()
        list_denounce = DenounceTextSerializer(list_all_denounce, many=True)
        return Response({"data": list_denounce.data}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        """
        pk = DenounceText model
        """
        try:
            denounces_data = DenounceText.objects.get(id=pk)
            serializer = DenounceTextSerializer(denounces_data)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        """
        create updating for each project
        """
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    {"data": True, "msg": "denounce created."},
                    status=status.HTTP_201_CREATED,
                )
        except Exception as e:
            return Response(
                {"data": False, "msg": f"{e}"}, status=status.HTTP_400_BAD_REQUEST
            )
