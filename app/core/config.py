from functools import lru_cache
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    # APP Config
    APP_TITLE_: str = "Youtube summarizer"
    APP_VERSION_: str = "0.1.0"
    APP_HOST_: str = "0.0.0.0"
    APP_PORT_: int = 8080
    API_VERSION_: str = "v1"
    DOCS_URL_: str = "/"
    OPEN_API_URL_: str = "/api/openapi.json"
    CORS_ORIGIN_: list = ["*"]
    SUMMARIZE_PROMPT_: str = "Summarize the video transcript in one paragraph."

    # Services
    OPEN_AI_KEY_: str

@lru_cache()
def get_app_config():
    config = Config()
    return config
