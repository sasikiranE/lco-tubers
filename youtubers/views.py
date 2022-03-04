from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def youtubers(request):
    return HttpResponse('Youtubers page')

def youtuber_details(requset, youtuber_id):
    return HttpResponse(f'Hi I am Youtuber {youtuber_id}')

def search(request):
    return HttpResponse('Search page')