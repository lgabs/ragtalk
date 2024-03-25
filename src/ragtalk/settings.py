import tomllib
from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, FilePath, SecretStr, Field


class Settings(BaseSettings):
    environment: str
    database_url: PostgresDsn
    params_path: FilePath = Field(default="/data/params.toml")
    openai_api_key: SecretStr
    knowledge_base_path: FilePath = Field(default="./data/knowledge_base.csv")


config = Settings()

with open(config.params_path, "rb") as file:
    chain_params = tomllib.load(file)
