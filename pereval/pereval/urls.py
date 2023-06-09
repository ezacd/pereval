from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from rest_app.views import PerevalViewSet

router = SimpleRouter()
router.register('pereval', PerevalViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('submitData/', include('rest_app.urls')),
] + router.urls
