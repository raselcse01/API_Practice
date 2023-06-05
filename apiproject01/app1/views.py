from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.

# model object - single student data
def student_detail(request, pk):
    stu = Student.objects.get(pk = pk)
    serializer = StudentSerializers(stu)

    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

    # return JsonResponse(serializer.data)



# Query set - All student data
def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializers(stu, many = True)

    # json_data = JSONRenderer().render(serializer.data)

    # return HttpResponse(json_data, content_type='application/json')

    return JsonResponse(serializer.data, safe=False)
