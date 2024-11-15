from django.urls import path
from . import views


app_name = "dashboard"

urlpatterns = [
    path("", views.admin_view, name="admin_view"),
    path("messages/", views.messages_view, name="messages_view"),
    path("new-project/", views.new_project_view, name="new_project_view"),
    path("admin-project-detail/", views.projrct_detail_admin_view, name="projrct_detail_admin_view"),
    path("search/", views.search_project, name="search_project"),
    path("update/", views.update_project, name="update_project"),
    path("delete/", views.delete_project, name="delete_project"),

]