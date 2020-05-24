from django.urls import path
from comments import views
from comments import views_ans

app_name = 'comment'

urlpatterns = [
    path('comment', views.CommentView.as_view({
        'get': 'list',
        'post': 'create'}), name='comment'),
    path('comments', views.CommentPublicView.as_view({
        'get': 'list'}), name='comment'),
    path('answer', views_ans.CommentResponseView.as_view({
        'get': 'list',
        'post': 'create'}), name='answer'),
]
