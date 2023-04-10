from django.db import models
from datetime import datetime


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    enrollment_date = models.DateField(max_length=50)
    birthday = models.DateField(max_length=50)
    group_name = models.CharField(max_length=50)


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    hire_date = models.DateField(max_length=50)
    birthday = models.DateField(max_length=50)


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    desciption = models.CharField(max_length=50)
    course_level = models.CharField(max_length=50, choices=(("A1", "begginer"),("A2", "Elementary"), ("B1", "pre-intermedia"), ("B2", "Intermedia")))
    course_duration = models.IntegerField(choices=((2, "2 month"),(4, "4 months"), (6, "6 months"), (6, "6 months")))
    fee = models.FloatField(default=0)


class Attendace(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    attendace_day = models.DateField(auto_now=True)
    attendace_status = models.CharField(max_length=50, choices=(("-", "absence"), ("+", "present")))


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    assessment = models.CharField(max_length=50, choices=(("2", "poor"),("3", "Satisfactory"), ("4", "good"), ("5", "excellent")))
    grade_day = models.DateField(auto_now=True)

# class FinalExam(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     exam_result = models.CharField( max_length=50, choices=((2, "failed"), (3, "Pass"), (4, "good"), (5, "excellent")))


class Material(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    material_name = models.CharField(max_length=50)
    material_description = models.TextField()
    material_link = models.CharField(max_length=200)


class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day_per_week = models.CharField(max_length=50)
    start_time = models.DateField()
    end_time = models.DateField()
    location = models.CharField(max_length=50)


class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    payment_date = models.DateField(auto_now=True)
    payment_amount = models.IntegerField()
