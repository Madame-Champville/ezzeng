from django.shortcuts import render
from django.views import generic

from .models import Student, Teacher, Course, Attendace, Grade, Material, Schedule, Payment


class StudentList(generic.ListView):
    model = Student
    template_name = 'student_list.html'

class TeacherList(generic.ListView):
    model = Teacher
    template_name = 'teacher_list.html'

class AboutList(generic.ListView):
    model = Teacher
    template_name = 'about_list.html'