from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    APPLICATION_NAME: str = "{{ cookiecutter.project_name }}"
    API_KEY: SecretStr = SecretStr("secret")