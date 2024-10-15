from app import create_app
from app.core.config import get_app_config

app_config = get_app_config()

app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="main:app",
        host=app_config.APP_HOST_,
        port=app_config.APP_PORT_,
        log_config=None,
        reload=True,
    )
