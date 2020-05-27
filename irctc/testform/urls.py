from django.urls import path, re_path
from . import views

app_name = 'testform'

urlpatterns = [
    path('', views.create_book_model_form , name='book_list'),    
]
