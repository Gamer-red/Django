from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('abaout/',views.about, name="about"),
    path('hello/<str:username>', views.hello, name="about"),
    path('projects/', views.projects, name="projects"),
    path('tasks/', views.tasks, name="tasks"),
    path('create_task/', views.create_task, name="create_ task"),
    path ('create_project/',views.create_project, name="create_project")
]