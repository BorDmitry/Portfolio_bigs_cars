from django.shortcuts import render
from .models import BigsCars


def index(request):
    projects = BigsCars.objects.all()
    return render(request, 'bigs_cars/index.html', {'projects': projects})
