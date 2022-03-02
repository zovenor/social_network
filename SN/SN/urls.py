from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('DjangoAdmin/', admin.site.urls),
    path('messenger/', include('messenger.urls')),
    path('', include('mainpage.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "mainpage.views.page_not_found_view"
