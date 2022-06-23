
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path,include
from . import views

urlpatterns =[
    path('',views.home, name='home'),

    path('accounts/', include('registration.backends.simple.urls')),
    path('logout/', auth_views.LogoutView.as_view(),{'next_page':'/'}, name='logout'),

    path('api/v1/access/token', views.getAccessToken, name='get_mpesa_access_token'),
    path('api/v1/online/lipa', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),

]