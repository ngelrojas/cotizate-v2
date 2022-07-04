from django.urls import path
from tags import views

app_name = 'tag'

urlpatterns = [
    path('tag', views.TagView.as_view({
        'get': 'list'}), 
         name='tags'
    )
]
