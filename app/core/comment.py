from django.db import models
from .user import User


class Comment(models.Model):
    """comment model"""

    discuss = models.CharField(max_length=200)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    campaings = models.IntegerField(default=0)
    parentid = models.IntegerField(default=0)

    def __str__(self):
        return self.users.first_name

    def get_all_comments_by_user(self, request):
        return Comment.objects.filter(users=request.user.id)

    def get_comments_by_id(self, commentId, request):
        return Comment.objects.get(id=commentId, users=request.user)

    def get_all_comment_by_campaingsId(self, campaing):
        return Comment.objects.filter(campaings=campaing)

    def get_all_comment_by_campaings_slug(self, campaing):
        return Comment.objects.filter(campaings=campaing)

    def get_all_ans_by_comment_user(self, request, parentID):
        return Comment.objects.filter(users=request.user.id, parentid=parentID)

    def get_all_ans_by_comment(self, parentID):
        return Comment.objects.filter(parentid=parentID)
