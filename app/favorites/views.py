from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.favorite import Favorite
from .serializers import FavoriteSerializer


class FavoriteView(viewsets.ModelViewSet):
    """Favorite
    - list: list favorites to current user
    - create: create favorite to current user
    - retrieve: retrieve favorite to current user and ID campaing
    - update: update favorite to current user and ID campaing
    """
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()

    def list(self, request):
        """list all favorites about current user"""
        try:
            current_fav = Favorite.objects.exclude(campaings=0).filter(
                users=request.user.id)
            serializer = self.serializer_class(current_fav, many=True)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'data': False,
                             'msg': f'{err}'},
                            status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        """create favorite to current user and campaing"""
        try:
            data = request.data.copy()
            data['users'] = request.user.id
            serializer = self.serializer_class(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'data': True,
                                 'msg': 'favorite saved.'},
                                status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response({'data': False,
                             'msg': f'{err}'},
                            status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        """retrieve favorite to current user and campaing"""
        try:
            current_fav = Favorite.get_retrieve_favorite(self, request, pk)
            serializer = self.serializer_class(current_fav)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'data': False,
                             'msg': f'{err}'},
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        """update favorite to current user and campaing"""
        try:
            current_fav = Favorite.get_retrieve_favorite(self, request, pk)
            serializer = self.serializer_class(
                current_fav,
                data=request.data,
                partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'data': True,
                                 'msg': 'update favorite.'},
                                status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'data': False,
                             'msg': f'{err}'},
                            status=status.HTTP_400_BAD_REQUEST)
