from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Heelo, World</h1><b>Welcome to my Library</b>")
