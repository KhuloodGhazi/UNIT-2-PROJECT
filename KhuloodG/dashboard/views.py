from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from main.models import Contact
from projects.models import Project



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
        )

        new_project.save()

        return redirect("main:main_view") 

    return render(request, 'dashboard/new_project.html')




def projrct_detail_admin_view(request:HttpRequest):

    return render(request, 'dashboard/admin_project_detail.html')




def search_project(request:HttpRequest):

    return render(request, 'dashboard/search_project.html')




def update_project(request:HttpRequest):

    return render(request, 'dashboard/update_project.html')




def delete_project(request:HttpRequest):

    return render(request, 'dashboard/delete_project.html')

