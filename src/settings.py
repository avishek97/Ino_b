from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='./env', extra='ignore')
    DB_CONNECTION: str

settings = Settings()