from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=32, help_text='Required.')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    
    def __init__(self, *args: Any, **kwargs: Any):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    def __init__(self, *args: Any, **kwargs: Any):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'  # Use all fields from the Employee model
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)

        # Set placeholders for each field
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter email'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter phone number'
        self.fields['hire_date'].widget.attrs['placeholder'] = 'Enter hire date'
        self.fields['job_title'].widget.attrs['placeholder'] = 'Enter job title'
        self.fields['salary'].widget.attrs['placeholder'] = 'Enter salary'
        self.fields['department'].widget.attrs['placeholder'] = 'Enter department'

        # Add 'required' class to each field
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.label = False
            if field.required:
                field.widget.attrs['required'] = 'required'