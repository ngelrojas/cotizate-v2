from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.phase import Phase
from core.campaing import Campaing
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

    def list(self, request, pk):
        """
        list all phases
        about the current campaing
        """
        try:
            campaing = Campaing.get_campaing_id(request, pk) 
            current_list_phase = Phase.get_all(campaing)
            serializer = self.serializer_class(current_list_phase, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )

    def retrieve(self, request, pk, cp):
        """retrieve phase current campaing_header_id, campaing_id"""
        try:
            current_phase = Phase.get_phase(cp, pk)
            serializer = self.serializer_class(current_phase)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )

    def create(self, request):
        """create phase"""
        try:
            pk = request.data.get('campaing_id')
            obj_campaing = Campaing.get_campaing_id(request, pk)
            resp = Phase.created(obj_campaing, request) 
            return Response(
                    {"data": resp, "msg": "phase created"},
                status=status.HTTP_201_CREATED,
            )
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, pk, cp):
        """update phase"""
        try:
            obj_campaing = Campaing.get_campaing_id(request, cp)
            resp = Phase.updated(obj_campaing, request, pk)
            return Response(
                    {"data": resp, "msg": "phase updated"},
                status=status.HTTP_200_OK,
            )
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk, cp):
        """delete reward"""
        try:

            resp = Phase.erase(cp, pk)
            return Response(
                    {"data": resp, "msg": "phase deleted."},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Exception as err:
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
