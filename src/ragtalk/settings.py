import tomllib
from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, FilePath, SecretStr


class Settings(BaseSettings):
    environment: str
    database_url: PostgresDsn
    params_path: FilePath
    openai_api_key: SecretStr


config = Settings.model_validate({})

with open(config.params_path, 'rb') as file:
    toml_data = tomllib.load(file)