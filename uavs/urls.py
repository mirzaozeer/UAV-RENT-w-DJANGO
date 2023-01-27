from django.urls import path
from .import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="index"),
    path('admin/', admin.site.urls),
    path("<int:uav_id>", views.detail, name="detail"),
    path("login/", views.home, name = "home"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)