from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('school/', include('school.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    # Serve Media contents only on dev server, on prod Nginx will take care
    # urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
    urlpatterns.extend(
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))

    # Serve root domain media contents
    urlpatterns.extend([
        path('favicon.ico', serve, {
             'path': 'img/favicon.ico', 'document_root': settings.STATIC_ROOT}),
    ])
