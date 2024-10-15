from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from anyio import to_thread
from .utils.headers import default_headers_injection
from .core.config import get_app_config
from .api import router
from .utils.logger import logger

app_config = get_app_config()

API_PREFIX = "/api"


@asynccontextmanager
async def lifespan(_: FastAPI):

    logger.info("Starting up")

    limiter = to_thread.current_default_thread_limiter()
    limiter.total_tokens = 1000

    yield

    logger.info("Shutting down...")


def create_app() -> FastAPI:

    app = FastAPI(
        title=app_config.APP_TITLE_,
        version=app_config.APP_VERSION_,
        docs_url=app_config.DOCS_URL_,
        openapi_url=app_config.OPEN_API_URL_,
        lifespan=lifespan,
    )

    app.include_router(
        router=router,
        prefix=f"{API_PREFIX}/{app_config.API_VERSION_}",
        dependencies=[Depends(default_headers_injection)],
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=app_config.CORS_ORIGIN_,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
