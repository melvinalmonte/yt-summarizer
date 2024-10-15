from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from app.api.summarize.services import SummarizeService

router = APIRouter()

ENDPOINT = "/summarize"

@router.get(
    ENDPOINT,
    response_class=StreamingResponse,
    summary="Summarize Youtube Video",
)
async def summarize_video(youtube_url: str) -> StreamingResponse:
    summarizer = SummarizeService(youtube_url)

    try:
        async def summary_generator():
            async for chunk in summarizer.summarize_video():
                yield chunk

        return StreamingResponse(summary_generator(), media_type="text/plain")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error: " + str(e))