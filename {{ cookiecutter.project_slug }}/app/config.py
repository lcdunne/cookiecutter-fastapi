from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    APPLICATION_NAME: str = "{{ cookiecutter.project_name }}"
    API_KEY: SecretStr
{% if cookiecutter.database != None %}
    DATABASE_ECHO: bool = False
{% endif %}
{% if cookiecutter.database == "sqlite" %}
    DATABASE_URL: str = "sqlite:///./app.db"
{% elif cookiecutter.database == "postgresql" %}
    DATABASE_URL: str
{% endif %}