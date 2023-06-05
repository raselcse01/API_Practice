
from django.contrib import admin
from django.urls import path, include
from app import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Registration router
router.register('singer', views.SingerViewSet, basename='singer')
router.register('song', views.SongViewsets, basename='song')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
