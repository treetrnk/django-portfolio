from django.shortcuts import render
from .models import *

def index(request):
    context = {
        'experience': Experience.objects.all(),
        'works': Work.objects.all(),
    }

    for c in Content.objects.all():
        context[c.name.lower() + '_text'] = {
            'name': c.name, 
            'body': c.body
        }

    return render(request, 'sections/home.html', context)
