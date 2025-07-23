from django.contrib import admin
from django.urls import path, include
from infrastructure.api.routers import router, extra_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    *extra_urls,
]
