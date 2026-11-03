from unittest.mock import Mock
import pytest
from openai import APIConnectionError, RateLimitError
from llm_client import generate_response


def create_mock_client(content="Python is a programming language."):
    client = Mock()

    response = Mock()
    response.choices = [
        Mock(message=Mock(content=content))
    ]

    client.chat.completions.create.return_value = response

    return client


def test_generate_response():
    client = create_mock_client()

    messages = [
        {"role": "user", "content": "What is Python?"}
    ]

    result = generate_response(client, messages)

    assert result == "Python is a programming language."
    client.chat.completions.create.assert_called_once()


def test_generate_response_with_empty_content():
    client = create_mock_client(content="")

    messages = [
        {"role": "user", "content": "What is Python?"}
    ]

    with pytest.raises(ValueError, match="empty response"):
        generate_response(client, messages)


def test_rate_limit_error():
    client = Mock()
    client.chat.completions.create.side_effect = RateLimitError(
        message="Rate limit exceeded",
        response=Mock(status_code=429, headers={}),
        body=None
    )

    with pytest.raises(RuntimeError, match="rate limit or quota"):
        generate_response(client, [{"role": "user", "content": "Hello"}])


def test_connection_error():
    client = Mock()
    client.chat.completions.create.side_effect = APIConnectionError(
        request=Mock()
    )

    with pytest.raises(RuntimeError, match="Unable to connect"):
        generate_response(client, [{"role": "user", "content": "Hello"}])