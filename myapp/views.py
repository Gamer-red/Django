from django.shortcuts import render
from django.http import HttpResponse
from .models import project
# Create your views hee.

def index(request):
    return HttpResponse("Index page")

def hello(request, username):
    return HttpResponse("<h2>Hello<h2> %s </h2>" % username)

def about(request):
    return HttpResponse("Solo estoy haciendo un abaut jaja")

def projects(request):
    return HttpResponse('projects')

def tasks(request):
    return HttpResponse('tasks')
