from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Project


# Create your views here.

def projects_view(request:HttpRequest):

    projects = Project.objects.all()

    return render(request, 'projects/all_projects.html', {'projects': projects})




def project_detail_view(request:HttpRequest):

    return render(request, 'projects/project_detail.html')




