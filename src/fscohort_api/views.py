from django.shortcuts import render
from fscohort.models import Student
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from rest_framework import status

# Create your views here.

def home_api(request):
    data = {
        "name":"Henry",
        "adress":"clarusway.com",
        "skills": ["python", "django"]
    }
    
    
    return JsonResponse(data)

@api_view(["GET", "POST"])
def student_list_create_api(request):
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Student created successfully !"
            }
            return Response(data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    























# def student_list_api(request):
#     if request.method == "GET":
#         students = Student.objects.all()
#         student_count = Student.objects.count()
#         student_data = serialize("python", students)
#         print(student_data)
#         data ={
#             "students":student_data,
#             "count":student_count
#         }
#         return JsonResponse(data)
    
# @csrf_exempt
# def student_create_api(request):
#     if request.method == "POST":
#         post_body = json.loads(request.body)
#         name = post_body.get("first_name")
#         lastname = post_body.get("last_name")
#         number = post_body.get("number")
        
#         student_data = {
#             "first_name":name,
#             "last_name":lastname,
#             "number":number
#         }
        
#         student_obj = Student.objects.create(**student_data)
#         data ={
#             "message":f"Student {student_obj.first_name} is created !"
#         }
#         return JsonResponse(data)

# def student_list_api(request):
#     if request.method == "GET":
#         students = Student.objects.all()
#         student_count = Student.objects.count()
#         student_list = []
#         for student in students:
#             student_list.append({
#                "firstname":student.first_name, 
#                "lastname":student.last_name,
#                "number":student.number,
#             })
        
#         data ={
#             "students":student_list,
#             "count":student_count
#         }
#         # data ={
#         #     "students":students,
#         #     "count":student_count
#         # }
#         return JsonResponse(data)
    
