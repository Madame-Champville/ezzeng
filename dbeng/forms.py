from .models import *
from django import forms

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['name', 'email', 'password']

class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = ['student', 'course_name', 'payment_method', 'payment_amount']