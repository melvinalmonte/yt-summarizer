from fastapi import APIRouter

from .summarize import api as summarize_video

router = APIRouter()

router.include_router(summarize_video.router, tags=["Summarize"])