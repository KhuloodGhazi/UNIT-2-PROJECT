from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


# Create your views here.

def projects_view(request:HttpRequest):

    return render(request, 'projects/all_projects.html')




def detail_view(request:HttpRequest):

    return render(request, 'projects/project_detail.html')




def new_project_view(request:HttpRequest):

    return render(request, 'projects/new_project.html')



