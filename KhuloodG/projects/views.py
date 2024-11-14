from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Project


# Create your views here.

def projects_view(request:HttpRequest):

    projects = Project.objects.all()

    return render(request, 'projects/all_projects.html', {'projects': projects})




def detail_view(request:HttpRequest):

    return render(request, 'projects/project_detail.html')




def new_project_view(request:HttpRequest):

    if request.method == "POST":
        new_project = Project(
            project_name=request.POST["project_name"],
            project_brief=request.POST["project_brief"],
            project_model=request.POST["project_model"],
            category=request.POST["category"],
        )

        new_project.save()

        return redirect("main:main_view") #new Pgae for added

    return render(request, 'projects/new_project.html')



