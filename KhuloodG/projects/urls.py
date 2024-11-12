from django.urls import path
from . import views


app_name = "projects"

urlpatterns = [
    path("all-projects/", views.projects_view, name="projects_view"),
    path("detail/", views.detail_view, name="detail_view"),
]