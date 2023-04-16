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

class BlogsList(generic.ListView):
    model = Material
    template_name = 'blogs_list.html'

class PostList(generic.ListView):
    model = Material
    template_name = 'post_list.html'

class EngTestList(generic.ListView):
    model = Material
    template_name = 'eng-test_list.html'

class CoursesList(generic.ListView):
    model = Course
    template_name = 'courses_list.html'

class CourseInnerList(generic.ListView):
    model = Course
    template_name = 'course-inner_list.html'

class CourseInnerIndividualList(generic.ListView):
    model = Course
    template_name = 'course-inner_individual_list.html'

class ContactList(generic.ListView):
    model = Material
    template_name = 'contact_list.html'