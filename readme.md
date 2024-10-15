# yt-summarizer

A FastAPI application that provides an API endpoint to generate concise summaries of YouTube videos using OpenAI's GPT models. The summaries are streamed in real-time, offering a responsive experience for users who want to quickly understand if a video is worth watching.

## Features

- **Summarize YouTube Videos**: Generate bullet-point summaries of the selected video.
- **Streaming Responses**: Receive summaries in real-time as they are generated.
- **Asynchronous Processing**: Efficient handling of multiple requests using async features.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/melvinalmonte/yt-summarizer.git
   cd yt-summarizer
    ```
2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. **Install the Requirements**

    ```bash
    pip install -r requirements.txt
    ```
4. **Set the OpenAI API Key**

    ```bash
    export OPEN_AI_KEY_=your_openai_key # on windows use `set OPEN_AI_KEY_=your_openai_key`
    ```
5. **Run the Application**

    ```bash
    python main.py
    ```
6. **Optional - Customize your summarize prompt**

    ```bash
    export SUMMARIZE_PROMPT_=your_summarize_prompt # on windows use `set SUMMARIZE_PROMPT_=your_summarize_prompt`
    ```