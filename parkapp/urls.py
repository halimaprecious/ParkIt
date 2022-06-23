from django.urls import re_path,path
from . import views

urlpatterns =[
    re_path('',views.home, name='home'),

    path('bookspace/', views.park, name='bookspace'),
]