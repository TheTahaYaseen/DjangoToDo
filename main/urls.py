
from . import views
from django.urls import path

urlpatterns = [
    path("", views.home_view, name = "home"),
    path("registration", views.registration_view, name = "registration"),
    path("login", views.login_view, name = "login"),
    path("todos", views.todos_view, name = "todos"),
    path("create_todo", views.create_todo_view, name = "create_todo"),
    path("update_todo", views.update_todo_view, name = "update_todo"),
    path("delete_todo", views.delete_todo_view, name = "delete_todo"),
    path("complete_todo", views.complete_todo_view, name = "complete_todo"),
    path("user_profile", views.user_profile_view, name = "user_profile"),
    path("update_user_profile", views.update_user_profile_view, name = "update_user_profile"),
    path("logout_user_profile", views.logout_user_profile_view, name = "logout_user_profile")
]