from django.urls import path
from . import views


app_name = "projects"

urlpatterns = [
    path("all-projects/", views.projects_view, name="projects_view"),
    path("new-project/", views.new_project_view, name="new_project_view"),
    path("detail/", views.detail_view, name="detail_view"),
]