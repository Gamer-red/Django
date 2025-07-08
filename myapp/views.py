from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("Hola estoy haciendo cambios juasjuas")

def about(request):
    return HttpResponse("Solo estoy haciendo un abaut jaja")
