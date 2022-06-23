from django.urls import re_path
from . import views

urlpatterns =[
    re_path('',views.home, name='home'),
    re_path('',views.pay, name='paynow')
]