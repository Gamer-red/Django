from django.shortcuts import render
from django.http import HttpResponse
from .models import project
from django.shortcuts import render
# Create your views hee.

def index(request):
    title = 'Django course' 
    return render (request,'index.html',{
        'title': title
    })

def hello(request, username):
    return HttpResponse("<h2>Hello<h2> %s </h2>" % username)

def about(request):
    username ={
        'name': 'jarol'
    }
    return render(request, 'about.html',{
        'username': username
    })

def projects(request):
    Projects = list(project.objects.values())
    return render(request, 'projects.html')

def tasks(request):
    # task = Task.objects.
    return render(request, 'task.html')
