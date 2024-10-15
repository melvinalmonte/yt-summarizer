from urllib.parse import urlparse, parse_qs

from openai import AsyncOpenAI
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

from app.core.config import get_app_config

app_config = get_app_config()

class SummarizeService:
    def __init__(self, youtube_url: str) -> None:
        self.youtube_url = youtube_url
        self.openai_client = AsyncOpenAI(api_key=app_config.OPEN_AI_KEY_)

    async def summarize_video(self):
        video_id = self._extract_video_id()
        if not video_id:
            raise ValueError("Invalid Youtube URL")

        formatter = TextFormatter()
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
        except Exception as e:
            raise ValueError("Failed to retrieve transcript" + str(e))

        text_formatted = formatter.format_transcript(transcript)

        stream = await self.openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": app_config.SUMMARIZE_PROMPT_,
                },
                {
                    "role": "user",
                    "content": f"Video Transcript: {text_formatted}"
                }

            ],
            stream=True,
        )

        async for chunk in stream:
            if chunk.choices[0] is not None:
                content = chunk.choices[0].delta.content
                if content:
                    yield content


    def _extract_video_id(self) -> str:
        parsed_url = urlparse(self.youtube_url)
        video_id = parse_qs(parsed_url.query).get("v")
        if not video_id:
            return ''
        return video_id[0]

