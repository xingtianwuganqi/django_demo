from django.conf.urls import url
from . import views

urlpatterns = [
    url('index$',views.index),
    url('(\d+)/(\d+)$',views.detail),
    url('name$',views.name),
    url('grades$',views.grades),
    url('students$',views.students),
    url('grades/(\d+)$',views.gradesStudents) # $ 表示结尾
]