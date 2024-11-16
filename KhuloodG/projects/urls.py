from django.urls import path
from . import views


app_name = "projects"

urlpatterns = [
    path("all-projects/", views.projects_view, name="projects_view"),
    path("detail/<int:project_id>", views.project_detail_view, name="project_detail_view"),
]