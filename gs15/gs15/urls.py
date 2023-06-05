
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentlist/', views.StudentList.as_view()),
    path('studentcreate/', views.StudentCreate.as_view()),
    path('studentretrive/<int:pk>/', views.StudentRetrive.as_view()),
    path('studentupdate/<int:pk>/', views.StudentUpdate.as_view()),
    path('studentdestroy/<int:pk>/', views.StudentDestroy.as_view()),

    # ListCreateAPIView
    path('studentlistcreate/', views.StudentListCreate.as_view()),
    path('studentretrivecreate/<int:pk>/', views.StudentRetriveCreate.as_view()),
    path('studentretrivedistroy/<int:pk>/', views.StudentRetriveDistroy.as_view()),
    path('studentretrivecrud/<int:pk>/', views.StudentRetriveCRUD.as_view()),
]
