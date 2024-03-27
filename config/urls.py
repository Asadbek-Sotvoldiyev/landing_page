from django.conf.urls.static import static
from . import settings
from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('users/', include('users.urls')),
    path('places/', include('places.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
