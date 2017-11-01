from django.shortcuts import render
from .models import *

def index(request):
    context = {
        'experience': Experience.objects.all(),
        'works': Work.objects.all(),
    }
    return render(request, 'sections/home.html', context)
