from django.urls import path
from . import views


app_name = "projects"

urlpatterns = [
    path("all-projects/", views.projects_view, name="projects_view"),
    path("detail/", views.project_detail_view, name="project_detail_view"),
]