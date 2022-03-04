from django.shortcuts import render
from . models import Slider

# Create your views here.

def home(request):
    sliders = Slider.objects.order_by('-updated').all()
    context = {
        'sliders' : sliders,
    }
    return render(request, 'webpages/home.html', context)

def about(request):
    return render(request, 'webpages/about.html')

def contact(request):
    return render(request, 'webpages/contact.html')
    
def services(request):
    return render(request, 'webpages/services.html')