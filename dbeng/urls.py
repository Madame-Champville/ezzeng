from django.urls import path

from . import views

urlpatterns = [
    path('', views.StudentList.as_view(), name='student_list'),
    path('/about', views.AboutList.as_view(), name='about_list'),
]