from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Contact
from django.contrib import messages




# Create your views here.

def main_view(request:HttpRequest):

    return render(request, 'main/home.html')




def contact_view(request:HttpRequest):

    if request.method == "POST":
        new_message = Contact(
            name=request.POST["name"],
            email=request.POST["email"],
            message=request.POST["message"]
        )

        new_message.save()

        messages.success(request, "Your message has been sent successfully!")
        
        return redirect("main:contact_view")

    return render(request, 'main/contact.html') 
