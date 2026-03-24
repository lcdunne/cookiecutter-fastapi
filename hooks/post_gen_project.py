import os
import shutil

project_size = "{{ cookiecutter.project_size }}"
database = "{{ cookiecutter.database }}"
include_tests = "{{ cookiecutter.include_tests }}"

if project_size == "small":
    large_project_directories = [
        "api",
        "client",
        "database",
        "exceptions",
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

    if database != "postgresql":
        os.remove(os.path.join("docker", "init.sql"))
else:  # large
    for module in ["database.py", "dependencies.py", "schemas.py"]:
        os.remove(os.path.join("app", module))

    if database == "none":
        shutil.rmtree(os.path.join("app", "database"))

    if database != "postgresql":
        os.remove(os.path.join("docker", "init.sql"))

if include_tests == "no":
    shutil.rmtree("tests")
    os.remove("pytest.ini")
