from django.urls import path,re_path
from . import views

urlpatterns =[
    path('',views.parkit,name='myparking'),
    # path('bookslot', views.booked_slot, name='parking'),

    path('bookslot/<slot_id>',views.booked_slot,name='bookslot'),

]