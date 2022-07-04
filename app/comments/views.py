from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.comment import Comment
from core.campaing import Campaing
from .serializers import CommentSerializer


class CommentView(viewsets.ModelViewSet):
    """
    private
    create comment registers users
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def list(self, request):
        """list all campang by user"""
        queryset = Comment.get_all_comments_by_user(self, request)
        serializer = self.serializer_class(queryset, many=True)
        return Response(
            {"data": serializer.data, "msg": "ok"}, status=status.HTTP_200_OK
        )

    def create(self, request):
        """
        create a comment with rules
        - campaing is public
        """
        try:
            current_campaing = Campaing.objects.get(
                id=request.data.get("campaings"), users=request.user, status=5
            )
            data_send = {
                "campaings": current_campaing.id,
                "users": request.user,
                "commnet_des": request.data.get("comment"),
            }
            serializer = self.serializer_class(data=data_send)
            if serializer.is_valid(raise_exeception=True):
                serializer.save()
                return Response(
                    {"data": True, "msg": "comment created."},
                    status=status.HTTP_201_CREATED,
                )
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )


class CommentPublicView(viewsets.ModelViewSet):
    """
    public comments
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def retrieve(self, request, pk=None):
        """
            list all comment by campaing
            pk = campaing id
        """
        try:
            queryset = Comment.objects.filter(campaings=pk)
            serializer = self.serializer_class(queryset, many=True)
            return Response(
                {"data": serializer.data}, status=status.HTTP_200_OK
            )
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )
