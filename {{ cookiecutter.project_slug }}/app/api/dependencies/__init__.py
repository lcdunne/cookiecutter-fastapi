from app.api.dependencies.auth import require_admin
{% if cookiecutter.database != "none" %}
from app.api.dependencies.db import get_db
{% endif %}
