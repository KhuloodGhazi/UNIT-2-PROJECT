from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


# Create your views here.

def main_view(request:HttpRequest):

    return render(request, 'main/home.html')




def contact_view(request:HttpRequest):

    return render(request, 'main/contact.html') #All the work is here 




def about_view(request:HttpRequest):

    return render(request, 'main/about.html')
