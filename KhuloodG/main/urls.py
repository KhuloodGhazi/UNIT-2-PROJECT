from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
    path("", views.main_view, name="main_view"),
    path("contact/", views.contact_view, name="contact_view"),
    path("about/", views.about_view, name="about_view"),

]