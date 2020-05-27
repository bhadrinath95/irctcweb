from django.urls import path, re_path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index , name='index'),    
    path('create/<int:id>', views.create, name='create'),
]
