
from django.contrib import admin
from django.urls import path,include, re_path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('parkapp.urls')),


    re_path(r'^accounts/', include('registration.backends.simple.urls')),
    re_path(r'^logout/', auth_views.logout_then_login), 
]

