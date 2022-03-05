from django.shortcuts import render, get_object_or_404
from . models import Youtuber
from django.db.models import Q

# Create your views here.
def youtubers(request):
    tubers = Youtuber.objects.order_by('-updated').all()
    cities = Youtuber.objects.values_list('city', flat=True).distinct()
    cameras = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    categories = Youtuber.objects.values_list('category', flat=True).distinct()

    if 'city' in request.GET:
        data = request.GET['city']
        if data:
            tubers = tubers.filter(city__iexact=data)

    if 'camera' in request.GET:
        data = request.GET['camera']
        if data:
            tubers = tubers.filter(camera_type__iexact=data)

    if 'category' in request.GET:
        data = request.GET['category']
        if data:
            tubers = tubers.filter(category__iexact=data)

    context = {
        'tubers' : tubers,
        'cities' : cities,
        'cameras' : cameras,
        'categories': categories,
    }
    return render(request, 'youtubers/youtubers.html', context)


def youtuber_details(request, youtuber_id):
    tuber = get_object_or_404(Youtuber, pk=youtuber_id)
    context = {
        'tuber' : tuber,
    }
    return render(request, 'youtubers/youtuber_details.html', context)


def search(request):
    tubers = Youtuber.objects.all()
    cities = Youtuber.objects.values_list('city', flat=True).distinct()
    cameras = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    categories = Youtuber.objects.values_list('category', flat=True).distinct()

    if 'keyword' in request.GET:
        data = request.GET['keyword']
        if data:
            tubers = tubers.filter(Q(name__icontains=data) | Q(description__icontains=data))

    if 'city' in request.GET:
        data = request.GET['city']
        if data:
            tubers = tubers.filter(city__iexact=data)

    if 'camera' in request.GET:
        data = request.GET['camera']
        if data:
            tubers = tubers.filter(camera_type__iexact=data)

    if 'category' in request.GET:
        data = request.GET['category']
        if data:
            tubers = tubers.filter(category__iexact=data)

    context = {
        'tubers' : tubers,
        'cities' : cities,
        'cameras' : cameras,
        'categories' : categories,
    }
    return render(request, 'youtubers/search.html', context)