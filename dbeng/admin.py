from django.contrib import admin
from .models import Student, Teacher, Course, Attendance, Grade, Material, Schedule, Payment, User, Assessment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'password']
    search_fields = ['name',]
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'address', 'enrollment_date', 'birthday']
    search_fields = ['first_name', 'last_name']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'address', 'hire_date', 'birthday']
    search_fields = ['first_name', 'last_name']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name', 'members', 'course_level', 'course_duration', 'fee']
    search_fields = ['course_name', 'description']

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'attendance_day', 'attendance_status']
    search_fields = ['student', 'course']

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'assessment']
    search_fields = ['student', 'assessment']

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'assessment', 'grade_day']
    search_fields = ['student', 'course', 'assessment']

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['course', 'material_name', 'material_description']
    search_fields = ['course', 'material_name']

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['course', 'day_per_week', 'start_time', 'end_time', 'location']
    search_fields = ['course', 'start_time', 'location']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['student', 'payment_date', 'payment_amount']
    search_fields = ['student', 'payment_date']