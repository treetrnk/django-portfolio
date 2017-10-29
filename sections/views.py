from django.shortcuts import render
from .models import Skills

def index(request):
    return render(request, 'sections/home.html', {'skills': Skills.objects.all()})
