from django.db import models
class project (models.Model):
    name = models.CharField(max_length= 200)

    def __str__(self):
        return self.name
# Create your models here.
 
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
       return self.title + " - " + self.project.name