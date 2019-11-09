from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', include('charts.urls')),
    path(r'', include('pages.urls')),
]
