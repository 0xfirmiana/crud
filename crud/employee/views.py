from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserLoginForm, EmployeeForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Employee 
from django.db.models import Q
from django.db import models


def index(request):
    if request.user.is_authenticated:
        records = Employee.objects.all() 
    else:
        records = []
    return render(request,'index.html', {'records': records})

def logout_user(request):
    logout(request)
    return redirect('index')


def signin(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']        

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Invalid username or password", extra_tags="alert-danger")
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error, extra_tags="alert-danger")

    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def add_employee(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Added Sucessfully!", extra_tags="alert-success")
            return redirect('index')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form':form})

def edit(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee) 
        if form.is_valid():
            form.save()
            messages.success(request, "Updated Successfully!", extra_tags="alert-success")
            return redirect('index')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit_record.html', {'form':form})

def delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    messages.success(request, "Deleted Successfully!", extra_tags="alert-success")
    return redirect('index')

def search(request):
    if not request.user.is_authenticated:
        return redirect('login')
    q = request.GET.get('q', '')
    if q:
        search_query = Q()
        for field in Employee._meta.fields:
            if isinstance(field, (models.CharField, models.TextField)):
                search_query |= Q(**{f"{field.name}__icontains": q})
        records = Employee.objects.filter(search_query)
        if not records:
            messages.error(request, "No records found!", extra_tags="alert-danger")
            return redirect('index')
        messages.success(request, f"Results for query: {q}", extra_tags="alert-success")
        return render(request, 'search.html', {'records':records})
    else:
        redirect('index')