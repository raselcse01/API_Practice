
from django.contrib import admin
from django.urls import path, include
from app import views
from rest_framework.routers import DefaultRouter

# Creating router object
router = DefaultRouter()

# Register studentviewset router
router.register('studentapi', views.StudentViewSet, basename='student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
