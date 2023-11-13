from django.shortcuts import render, redirect
from .forms import SignUpForm, UserLoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def index(request):
    return render(request,'index.html')

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