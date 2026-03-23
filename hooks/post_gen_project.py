import os
import shutil

project_size = "{{ cookiecutter.project_size }}"
database = "{{ cookiecutter.database }}"

if project_size == "small":
    large_project_directories = [
        "api",
        "client",
        "database",
        "middleware",
        "repository",
        "schemas",
        "services",
        "utils",
    ]

    for directory in large_project_directories:
        shutil.rmtree(os.path.join("app", directory))

    if database == "none":
        os.remove(os.path.join("app", "database.py"))
else:
    for module in ["database.py", "dependencies.py"]:
        os.remove(os.path.join("app", module))

    if database == "none":
        shutil.rmtree(os.path.join("app", "database"))
