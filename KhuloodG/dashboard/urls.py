from django.urls import path
from . import views


app_name = "dashboard"

urlpatterns = [
    path("", views.admin_view, name="admin_view"),
    path("messages/", views.messages_view, name="messages_view"),
]