from django.urls import path
from . import views


app_name = "dashboard"

urlpatterns = [
    path("admin-dashboard/", views.admin_view, name="admin_view"),
    path("message/", views.message_view, name="message_view"),
]