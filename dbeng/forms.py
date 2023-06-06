from .models import *
from django import forms

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'email', 'courses']

class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = ['student', 'course_name', 'payment_amount']