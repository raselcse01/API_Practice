import io
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
# from rest_framework.response import Response
# from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated



# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondaata = JSONParser().parse(stream)
        id = pythondaata.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondaata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondaata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.errors) 
        return HttpResponse(json_data, content_type='application/json')
    
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondaata = JSONParser().parse(stream)
        id = pythondaata.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=pythondaata, partial = True)
        # serializer = StudentSerializer(stu, data=pythondaata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Updated !!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondaata = JSONParser().parse(stream)
        id = pythondaata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg':'Data Deleted'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(res, safe=True)