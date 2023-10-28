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
    with open(f"{html_file}.html") as file:
        file.write()