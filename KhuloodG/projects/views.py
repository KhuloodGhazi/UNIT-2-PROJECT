from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Project


# Create your views here.

def projects_view(request:HttpRequest):

    projects = Project.objects.all()

    return render(request, 'projects/all_projects.html', {'projects': projects})




def project_detail_view(request:HttpRequest, project_id: int):
    
    project = get_object_or_404(Project, pk=project_id)

    return render(request, 'projects/project_detail.html', {"project": project})




