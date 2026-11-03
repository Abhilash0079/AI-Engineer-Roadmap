import os
from dotenv import load_dotenv

def load_config():
    """Load and validate application configuration."""
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is missing. Please configure it in your .env file."
        )

    return {
        "api_key": api_key
    }
