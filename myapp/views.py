from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import project, Task # Importar con mayúscula correcta
from .forms import CreateNewTask,CreateNewProject

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

def create_task(request):
    if request.method == 'POST':
        form = CreateNewTask(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            Task.objects.create(title=title, description=description, project_id=2)
            return redirect("tasks")  # Redirige a tu lista de tareas u otra vista
    else:
        form = CreateNewTask()

    return render(request, 'create_task.html', {'form': form})

def create_project(request):
   if request.method == 'GET':
       return render(request, 'create_project.html',{
           'form': CreateNewProject()
       })
   else:
       print(request.POST)
       projects = project.objects.create(name=request.POST["name"])
       print(projects)
       return render(request,'create_project.html',{
           'form': CreateNewProject()
       }, redirect("projects")
       )

def project_detail(request, id):
    Project= get_object_or_404(project, id=id)
    task= Task.objects.filter(project_id=id)
    return render (request, 'detail.html', {
        'project': Project,
        'task': task
    })