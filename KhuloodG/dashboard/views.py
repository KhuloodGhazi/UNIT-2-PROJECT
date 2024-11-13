from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.

def admin_view(request:HttpRequest):

    return render(request, 'dashboard/admin_dashboard.html')




def message_view(request:HttpRequest):

    return render(request, 'dashboard/message.html')

