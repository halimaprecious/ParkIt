
from django.contrib import admin
from django.urls import path,include, re_path

from django.conf import settings

# from django.conf.urls import include, re_path


from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('',include('parkapp.urls')),
    re_path(r'^accounts/', include('registration.backends.simple.urls')),
    re_path(r'^logout/', auth_views.logout_then_login),
  
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
