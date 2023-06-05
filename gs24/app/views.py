from django.shortcuts import render
from .models import Student
from rest_framework import viewsets
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated
from app.customauth import CustomAuthentication

# Create your views here.

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializers_classes = StudentSerializer
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]
