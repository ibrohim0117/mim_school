from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from root import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
# ] + static(settings.STATIC_URL, docoment_root=settings.STATIC_ROOT)
] + static(settings.STATIC_URL, docoment_root=settings.STATICFILES_DIRS) + static(settings.MEDIA_URL, docoment_root=settings.MEDIA_ROOT)

