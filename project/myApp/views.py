from django.shortcuts import render
from .models import Grades,Students
# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("sunck is a good man")

def detail(request,num):
    return HttpResponse("detail-%s"%num)

def name(request):
    return HttpResponse("you name is lili")

def grades(request):
    # 去模板里取数据
    grades_list = Grades.objects.all()
    # 将数据传递给模板，模板再渲染页面，将页面返回给浏览器
    return render(request,"myApp/grades.html",{"grades":grades_list})

def students(request):
    students_list = Students.objects.all()
    return render(request,"myApp/students.html",{"students": students_list})

def gradesStudents(request,num):
    grade = Grades.objects.get(pk=num)
    studentList= grade.students_set.all()
    return render(request,"myApp/students.html",{"students": studentList})


