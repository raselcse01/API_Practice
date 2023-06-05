from django.shortcuts import render

from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
# Create your views here.

class StudentSerializer(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # single vabe class e authentication use kora 
    authentication_classes = [BasicAuthentication]
    # authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    
