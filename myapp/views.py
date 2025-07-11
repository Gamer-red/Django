from django.shortcuts import render
from django.http import HttpResponse
from .models import project, Task  # Importar con mayúscula correcta

def index(request):
    title = 'Django course' 
    return render(request, 'index.html', {
        'title': title
    })

def hello(request, username):
    return HttpResponse("<h2>Hello</h2> %s" % username)

def about(request):
    username = {
        'name': 'jarol'
    }
    return render(request, 'about.html', {
        'username': username
    })

def projects(request):
    projects = project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'task.html', {
        'tasks': tasks
    })
