# from django.core.files.storage import FileSystemStorage
# from rest_framework import viewsets
# from rest_framework import status
# from rest_framework.response import Response
# from .serializers import UpdatingSerializer
# from core.updating import Updating
# from core.campaing import CampaingHeader


# class UpdatingPublicView(viewsets.ModelViewSet):
#     """
#     retrieve
#         - get all updateing
#     """

#     serializer_class = UpdatingSerializer
#     queryset = Updating.objects.all()

#     def retrieve(self, request, pk):
#         """
#         list tags about campaing
#         """
#         try:
#             camp_id = CampaingHeader.objects.get(id=pk)
#             list_updating = Updating.objects.filter(header=camp_id)
#             serializer = self.serializer_class(list_updating, many=True)

#             return Response({"data": serializer.data}, status=status.HTTP_200_OK)

#         except Exception as err:
#             return Response(
#                 {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
#             )
