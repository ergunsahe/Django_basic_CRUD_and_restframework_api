from django.shortcuts import get_object_or_404, render
from fscohort.models import Student
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse
# -------------------------------------
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from rest_framework import status
# --------------------------------------
from rest_framework.views import APIView
#-------------------------------------
from rest_framework import generics
#-------------------------------------
from rest_framework import mixins


# Create your views here.

def home_api(request):
    data = {
        "name":"Henry",
        "adress":"clarusway.com",
        "skills": ["python", "django"]
    }
    
    
    return JsonResponse(data)



# generics class base rest framework api

class StudentList(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

# class StudentList(generics.ListAPIView):
#     serializer_class = StudentSerializer
#     queryset = Student.objects.all()
# class StudentCreate(generics.CreateAPIView):
#     serializer_class = StudentSerializer
#     queryset = Student.objects.all()

class StudentUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = "id"



# class base mixins rest framework
# class Student(generics.GenericAPIView, mixins.ListModelMixin,mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
#     serializer_class = StudentSerializer
#     queryset = Student.objects.all()
#     lookup_field = "id"
    
#     def get(self, request, id=None):
#         if id:
#             return self.retrieve(request)
#         else:
#             return self.list(request)
        
#     def post(self, request):
#         return self.create(request)
    
#     def put(self, request, id=None):
#         return self.update(request, id)
    
#     def delete(self, request, id):
#         return self.destroy(request, id)
            






# class base with rest framework api

# class StudentList(APIView):
#     def get(self, request):
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
        
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return  Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    
# class StudentUpdateDelete(APIView):
#     def get_object(self, id):
#         try:
#             return Student.objects.get(id=id)
#         except Student.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#     def get(self, request, id):
#         student = self.get_object(id)
#         # student = get_object_or_404(Student, id=id)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)
    
#     def put(self, request, id):
#         student = self.get_object(id)
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 "message": "Student updated successfully !"
#             }
#             return Response(data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, id):
#         student = self.get_object(id)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
            




# with rest framework functional API

# @api_view(["GET", "POST"])
# def student_list_create_api(request):
#     if request.method == "GET":
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
        
#         return Response(serializer.data)
    
#     elif request.method == "POST":
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             # student = form.save(commit=False)
#             # student.teacher = request.user
#             # student.save()
#             serializer.save()
#             data = {
#                 "message": "Student created successfully !"
#             }
#             return Response(data, status=status.HTTP_201_CREATED)
#         return  Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)



# @api_view(["GET", "PUT", "DELETE"])   
# def student_get_update_delete(request, id):
#     student = get_object_or_404(Student, id=id)
#     if request.method == "GET":
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)
#     if request.method == "PUT":
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             # serializer.save(teacher=request.user)
#             serializer.save()
#             data={
#                 "message": "Student updated successfully!"
#             }
#             return Response(data)
#         return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
#     if request.method == "DELETE":
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# without rest framework functional API

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
    
