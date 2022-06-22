from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns=[
    path('bookspace/', views.park, name='bookspace'),
]