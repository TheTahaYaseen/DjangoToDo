from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request):
    # Home View Would Contain Recent Todos Of People (Globally)
    context = {}
    return render(request, "main/home_view.html", context)

def registration_view(request):
    # Allows User To Register
    context = {}
    return render(request, "main/registration_view.html", context)

def login_view(request):
    # Allows User To Login
    context = {}
    return render(request, "main/login_view.html", context)

def todos_view(request):
    # Shows The User's Todos With The Actions
    context = {}
    return render(request, "main/todos_view.html", context)

def create_todo_view(request):
    # Will Contain All Attributes Inputs
    context = {}
    return render(request, "main/create_todo_view.html", context)

def update_todo_view(request):
    # Will Contain All Attributes Inputs
    context = {}
    return render(request, "main/update_todo_view.html", context)

def delete_todo_view(request):
    # Will Delete Todo With A Confirmation Check
    context = {}
    return render(request, "main/delete_todo_view.html", context)

def complete_todo_view(request):
    # Will Require User To Submit Atleast One Piece Of Media According To Task
    context = {}
    return render(request, "main/complete_todo_view.html", context)

def user_profile_view(request):
    # Will Display User's Name And Email Along With His Completed Todos Having Medias In Them
    context = {}
    return render(request, "main/user_profile_view.html", context)

def update_user_profile_view(request):
    # Will Display Form To Update Username, Email Or Password
    context = {}
    return render(request, "main/update_user_profile_view.html", context)

def logout_user_profile_view(request):
    # Will Directly Logout And Redirect User
    context = {}
    return render(request, "main/logout_user_profile_view.html", context)
