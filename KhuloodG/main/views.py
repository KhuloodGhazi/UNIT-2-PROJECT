from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail




# Create your views here.

def main_view(request:HttpRequest):

    return render(request, 'main/home.html')




def contact_view(request:HttpRequest):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if not Contact.objects.filter(name=name, email=email, message=message).exists():
            new_message = Contact(name=name, email=email, message=message)
            new_message.save()
            
            subject = "New Message from Your Website"
            email_content = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"
            from_email = email
            recipient_list = ['khulood.u97@gmail.com']
            
            try:
                send_mail(subject, email_content, from_email, recipient_list)
                messages.success(request, "Your message has been sent successfully!")
                
            except Exception as e:
                print("Email send error:", e) 
                messages.error(request, "There was an error sending your message. Please try again.")
                
        else:
            messages.info(request, "It seems you've already submitted this message.")
  
        
        return redirect("main:contact_view")
    
    return render(request, 'main/contact.html')