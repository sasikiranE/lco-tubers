from django.shortcuts import render, get_object_or_404
from . models import Youtuber

# Create your views here.
def youtubers(request):
    tubers = Youtuber.objects.order_by('-updated').all()
    context = {
        'tubers' : tubers,
    }
    return render(request, 'youtubers/youtubers.html', context)


def youtuber_details(request, youtuber_id):
    tuber = get_object_or_404(Youtuber, pk=youtuber_id)
    context = {
        'tuber' : tuber,
    }
    return render(request, 'youtubers/youtuber_details.html', context)

def search(request):
    pass