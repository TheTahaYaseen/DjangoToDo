import os


html_files = [
    "home_view",
    "registration_view",
    "login_view",
    "todos_view",
    "create_todo_view",
    "update_todo_view",
    "delete_todo_view",
    "complete_todo_view",
    "user_profile_view",
    "update_user_profile_view",
    "logout_user_profile_view"
]

for html_file in html_files:
    os.system("cd ..")
    with open(f"main/templates/main/{html_file}.html", "w") as file:
        file.write(
            """
{% extends "layout.html" %}

{% block main %}

{% endblock main %}
            """
        )