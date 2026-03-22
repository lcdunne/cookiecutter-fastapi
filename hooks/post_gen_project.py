import os

if "{{ cookiecutter.database }}" == "none":
    os.remove(os.path.join("app", "database.py"))
