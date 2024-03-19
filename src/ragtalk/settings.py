from decouple import Csv, Config
import tomllib

config = Config("../.env")

DATABASE_URL = config("DATABASE_URL")
# Read the .toml file
with open('params.toml', 'rb') as file:
    toml_data = tomllib.load(file)