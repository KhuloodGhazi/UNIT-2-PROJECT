from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Contact



# Create your views here.

def main_view(request:HttpRequest):

    return render(request, 'main/home.html')




def contact_view(request:HttpRequest):

    if request.method == "POST":
        new_message = Contact(
            name=request.POST["name"],
            email=request.POST["Email"],
            message=request.POST["message"]
        )

        new_message.save()
        return redirect("main:main_view") #Need to create a new page & a message page for dashborad

    return render(request, 'main/contact.html') 
