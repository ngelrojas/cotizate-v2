from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.phase import Phase
from core.queries.phaseQuery import PhaseQuery
from .serializers import PhaseSerializer


class PhaseView(viewsets.ViewSet):
    """
    list:
        - list all phase
        about the current phase
    """

    serializer_class = PhaseSerializer
    queryset = Phase.objects.all()

    def list(self, request):
        """
        list all phases
        about the current campaing
        """
        try:
            current_list_phase = PhaseQuery.get_list_phase(request.data.get("header"))
            serializer = self.serializer_class(current_list_phase, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Phase.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )

    def retrieve(self, request, pk, he):
        """retrieve phase current campaing_header_id, campaing_id"""
        try:
            current_phase = PhaseQuery.retrieve_phase(pk, he)
            serializer = self.serializer_class(current_phase)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Phase.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )

    def create(self, request):
        """create phase"""
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    {"data": "phase saved."},
                    status=status.HTTP_201_CREATED,
                )
        except Phase.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )

    def update(self, request, pk, he):
        """update reward"""
        try:
            current_phase = PhaseQuery.retrieve_phase(pk, he)
            serializer = self.serializer_class(current_phase, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    {"data": "phase updated."},
                    status=status.HTTP_200_OK,
                )
        except Phase.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, pk, he):
        """delete reward"""
        try:

            current_phase = PhaseQuery.retrieve_phase(pk, he)
            current_phase.delete()
            return Response(
                {"data": " phase deleted."},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Phase.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )


class PhaseListView(viewsets.ViewSet):
    """
    list:
        - list all phase
        about the current phase
    """

    serializer_class = PhaseSerializer
    queryset = Phase.objects.all()

    def list(self, request, pk=None):
        """retrieve phase current campaing_header_id, campaing_id"""
        try:
            current_phases = PhaseQuery.get_list_phase(pk)
            serializer = self.serializer_class(current_phases, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )
