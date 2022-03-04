from django.shortcuts import render
from . models import Slider, Team

# Create your views here.

def home(request):
    sliders = Slider.objects.order_by('-updated').all()
    team_members = Team.objects.order_by('created').all()
    context = {
        'sliders' : sliders,
        'team_members' : team_members,
    }
    return render(request, 'webpages/home.html', context)

def about(request):
    return render(request, 'webpages/about.html')

def contact(request):
    return render(request, 'webpages/contact.html')
    
def services(request):
    return render(request, 'webpages/services.html')