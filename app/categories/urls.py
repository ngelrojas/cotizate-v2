from django.urls import path
from categories import views

app_name = 'category'

urlpatterns = [
    path('category', views.CategoryView.as_view({
        'get': 'list'}), name='categories')
]
