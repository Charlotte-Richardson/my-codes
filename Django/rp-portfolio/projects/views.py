from django.shortcuts import render
from projects.models import Project

def project_index(request):
    projects = Project.objects.all() #query of all objects
    context = { #dictionary
        'projects': projects
    }
    return render(request, 'project_index.html', context)
    #combines template with context dictionary

def project_detail(request, pk):
    project = Project.objects.get(pk=pk) #query of primary key for each project
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)