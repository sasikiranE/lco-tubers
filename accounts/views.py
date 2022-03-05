from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'username or password is incorrect')
    
    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'logged out successfully')
    return redirect('login_user')


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "password's doesn't match!")
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'username already exists')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'email already exists')
        else:
            user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
            user.save()
            messages.success(request, 'registered succesfully.')
            return redirect('login_user')

    return render(request, 'accounts/register.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')