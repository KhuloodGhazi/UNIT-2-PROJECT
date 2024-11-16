from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from main.models import Contact
from projects.models import Project
from django.contrib import messages




# Create your views here.

def admin_view(request:HttpRequest):

    return render(request, 'dashboard/admin_dashboard.html')




def messages_view(request:HttpRequest):
    
    messages = Contact.objects.all().order_by('-created_at')

    return render(request, 'dashboard/messages.html', {'messages': messages})




def new_project_view(request:HttpRequest):

    if request.method == "POST":
        new_project = Project(
            project_name=request.POST["project_name"],
            project_brief=request.POST["project_brief"],
            project_model=request.POST["project_model"],
            category=request.POST["category"],
            project_explanation=request.POST["project_explanation"],
            read_more_link=request.POST["read_more_link"],
            year=int(request.POST["year"]),
            image=request.FILES["image"],
            )
        
        new_project.save()
        messages.success(request, "Project created successfully!")

        return redirect("main:main_view")

    return render(request, 'dashboard/new_project.html')




def project_detail_admin_view(request:HttpRequest, project_id: int):

    project = get_object_or_404(Project, pk=project_id)

    return render(request, 'dashboard/admin_project_detail.html', {"project": project})




def search_project(request:HttpRequest):

    return render(request, 'dashboard/search_project.html')




def update_project(request:HttpRequest, project_id: int):

    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.project_name=request.POST.get("project_name", project.project_name)
        project.project_brief=request.POST.get("project_brief", project.project_brief)
        project.project_model=request.POST.get("project_model", project.project_model)
        project.category=request.POST.get("category", project.category)
        project.project_explanation=request.POST.get("project_explanation", project.project_explanation)
        project.read_more_link=request.POST.get("read_more_link", project.read_more_link)
        project.year=request.POST.get("year", project.year)

        if request.FILES.get("image"):
            project.image=request.FILES["image"]

        project.save()    
        messages.success(request, "Project created successfully!")


        return redirect("dashboard:project_detail_admin_view", project_id=project.id)

    return render(request, 'dashboard/update_project.html', {"project": project})




def delete_project(request:HttpRequest, project_id: int):

    project = get_object_or_404(Project, pk=project_id)
    
    project.delete()

    messages.success(request, "Project deleted successfully!")
    return redirect('dashboard:admin_view')

#return render(request, 'dashboard/delete_project.html', {"project": project})

