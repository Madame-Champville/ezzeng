from .models import *
from django import forms

class UserForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'phone', 'email', 'course']

class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'phone', 'email', 'course']