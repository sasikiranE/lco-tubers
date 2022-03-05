from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login_user(request):
    return HttpResponse('Login page')


def logout_user(request):
    return HttpResponse('Logout page')


def register_user(request):
    return HttpResponse('register page')


def dashboard(request):
    return HttpResponse('Dashboard page')