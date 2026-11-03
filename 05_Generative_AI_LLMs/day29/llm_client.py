from openai import OpenAI, APIConnectionError, APIStatusError, RateLimitError


def create_llm_client(api_key):
    """Create an OpenAI API client."""
    return OpenAI(api_key=api_key)


def generate_response(client, messages, model="gpt-4o-mini"):
    """Send messages to the LLM and return its response."""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages
        )

        content = response.choices[0].message.content

        if not content:
            raise ValueError("The LLM returned an empty response.")

        return content

    except RateLimitError as error:
        raise RuntimeError("API rate limit or quota exceeded.") from error

    except APIConnectionError as error:
        raise RuntimeError("Unable to connect to the OpenAI API.") from error

    except APIStatusError as error:
        raise RuntimeError(
            f"OpenAI API returned status code {error.status_code}."
        ) from error