from django.shortcuts import render
import requests
from django.http import HttpResponse
def home(request):
    return render(request, 'home.html')
# Create your views here.
