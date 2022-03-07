from http import server
from django.contrib import admin
from django.urls import path  , include,re_path
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('store.urls')),
   
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
