from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student

# Create your views here.
def home_view(request):
    # form = StudentForm()
    # context = {
    #     "title": "clarusway",
    #     "sec_tit":"<b>ankara</b>",
    #     "dict_1":{"django": "best framework"},
    #     "my_list":[1,2,3],
    #     "form":form
        
    # }
    return render(request, "fscohort/home.html")

# def about_view(request):
#     return HttpResponse("about page")

def student_list(request):
    students= Student.objects.all()
    context = {
        "students":students
    }
    
    return render(request, "fscohort/student_list.html", context)

def student_add(request):
    form= StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
        "form":form
    }
    
    return render(request, "fscohort/student_add.html", context)

def student_detail(request, id):
    student= Student.objects.get(id=id)
    context ={
        "student":student
    }
    return render(request, "fscohort/student_detail.html", context)

def student_delete(request, id):
    # student = get_object_or_404(Student, id=id)
    student= Student.objects.get(id=id)
    context = {
        "student":student
    }
    
    if request.method == "POST":
        student.delete()
        return redirect("list")
    
    return render(request, "fscohort/student_delete.html", context)

def student_update(request, id):
    # student = get_object_or_404(Student, id=id)
    student= Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
        "student":student,
        "form": form
    }
    
    return render(request, "fscohort/student_update.html", context)