from django.urls import path,include

from django.contrib.auth import views as auth_views
from . import views

urlpatterns =[
    path('',views.home, name='home'),

    path('accounts/', include('registration.backends.simple.urls')),
    path('logout/', auth_views.LogoutView.as_view(),{'next_page':'/'}, name='logout'),
]