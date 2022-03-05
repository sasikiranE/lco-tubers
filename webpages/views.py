from django.shortcuts import render
from . models import Slider, Team, ContactUs
from youtubers.models import Youtuber
from django.contrib import messages

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
    if request.method == 'POST':
        fullname = request.POST['fullname']
        phoneno = request.POST['phoneno']
        email = request.POST['email']
        company_name = request.POST['company_name']
        subject = request.POST['subject']
        message = request.POST['message']

        obj = ContactUs(fullname=fullname, phoneno=phoneno, email=email, company_name=company_name, subject=subject, message=message)
        obj.save()
        messages.success(request, "Thank's for reaching out to us!")
    return render(request, 'webpages/contact.html')