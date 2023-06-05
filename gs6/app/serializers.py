from django.shortcuts import render
from rest_framework import serializers
from .models import Student

# Create your views here.

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        field = ['name', 'roll', 'city']