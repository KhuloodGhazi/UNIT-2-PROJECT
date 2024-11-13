from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from main.models import Contact


# Create your views here.

def admin_view(request:HttpRequest):

    return render(request, 'dashboard/admin_dashboard.html')




def messages_view(request):
    
    messages = Contact.objects.all()

    return render(request, 'dashboard/messages.html', {'messages': messages})

