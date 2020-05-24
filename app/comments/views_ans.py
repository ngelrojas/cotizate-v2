from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.comment import Comment
from .serializers import CommentSerializer


class CommentResponseView(viewsets.ModelViewSet):
    """private comment answers"""
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def list(self, request):
        """list all answer comment by comment ID"""
        queryset = Comment.get_all_ans_by_comment(
            self, request.data.get('parentid'))
        serializer = self.serialzier_class(queryset, many=True)
        return Response(
            {'data': serializer.data},
            status=status.HTTP_200_OK)

    def create(self, request):
        """create answer to comment"""
        serializer = self.serialzier_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'data': 'comment created.'},
                            status=status.HTTP_201_CREATED)
        return Response({'error': 'somthing wrong'},
                        status=status.HTTP_404_NOT_FOUND)
