from django.shortcuts import render
from .models import Szklarnia
# Create your views here.

def index(request):
    parametry = Szklarnia.objects.all()
    return render(request, 'index.html', {'parametry':parametry})