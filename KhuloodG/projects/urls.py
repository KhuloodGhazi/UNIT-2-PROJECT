from django.urls import path
from . import views


app_name = "projects"

urlpatterns = [
    path("projects/", views.projects_view, name="projects_view"),
]