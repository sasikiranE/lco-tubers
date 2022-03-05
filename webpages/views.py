from django.shortcuts import render
from . models import Slider, Team
from youtubers.models import Youtuber

# Create your views here.

def home(request):
    sliders = Slider.objects.order_by('-updated').all()
    team_members = Team.objects.order_by('-created').all()
    featured_youtubers = Youtuber.objects.filter(is_featured=True).all()[:10]
    youtubers = Youtuber.objects.order_by('-updated').all()[:10]
    context = {
        'sliders' : sliders,
        'team_members' : team_members,
        'featured_youtubers' : featured_youtubers,
        'youtubers' : youtubers,
    }
    return render(request, 'webpages/home.html', context)


def about(request):
    team_members = Team.objects.order_by('-created').all()
    context = {
        'team_members' : team_members,
    }
    return render(request, 'webpages/about.html', context)


def contact(request):
    return render(request, 'webpages/contact.html')