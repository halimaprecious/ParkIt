
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path,include, re_path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('parkapp.urls')),
    
    path('accounts/', include('registration.backends.simple.urls')),
    path('logout/', auth_views.logout_then_login), 
]

