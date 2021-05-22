from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializers import ContactSerializer
from core.denounce import Contact


class ContactView(viewsets.ModelViewSet):
    """
    retrieve
        - get all contact
    """

    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def list(self, request):
        list_all_contact = Contact.objects.all()
        list_contact = self.serializer_class(list_all_contact)
        return Response({"data": list_contact.data}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        """
        pk =  contact id
        """
        try:
            contact_data = Contact.objects.get(id=pk)
            serializer = self.serializer_class(denounces_data)
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
                    {"data": True, "msg": "contact created."},
                    status=status.HTTP_201_CREATED,
                )
        except Exception as e:
            return Response(
                {"data": False, "msg": f"{e}"}, status=status.HTTP_400_BAD_REQUEST
            )
