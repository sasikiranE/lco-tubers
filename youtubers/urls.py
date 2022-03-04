from django.urls import path
from . import views

urlpatterns = [
    path('', views.youtubers, name='youtubers'),
    path('<int:youtuber_id>/', views.youtuber_details, name='youtuber_details'),
    path('search/', views.search, name='search'),
]