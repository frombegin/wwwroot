from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Slide

# Create your views here.

def index(request):
    return HttpResponse('Welcome to Truman\'s World!');


class SlideList(ListView):

    model = Slide
