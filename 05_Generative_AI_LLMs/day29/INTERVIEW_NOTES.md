# Day 29 — LLM APIs: Interview Notes

## 1. What is an LLM?

An LLM (Large Language Model) is an AI model trained on large amounts of text to understand and generate human-like language.

Examples include GPT models, Claude, and Gemini.

## 2. What is an LLM API?

An LLM API allows a software application to communicate with a language model.

A Python application sends a request containing messages and receives a generated response.

**Typical flow:**

1. Load API credentials.
2. Create an API client.
3. Prepare conversation messages.
4. Send the request.
5. Extract the model response.
6. Display or process the response.

## 3. What is an API key?

An API key is a credential used to authenticate an application when accessing an API.

It should be stored securely in an environment variable rather than hardcoded into source code.

Example:

```python
import os

api_key = os.getenv("OPENAI_API_KEY")
```

## 4. What are system, user, and assistant roles?

- **system:** Defines the assistant's behavior and instructions.
- **user:** Contains the user's input.
- **assistant:** Contains the assistant's generated response.

Example:

```python
messages = [
    {
        "role": "system",
        "content": "You are a helpful Python tutor."
    },
    {
        "role": "user",
        "content": "Explain Python functions."
    }
]
```

## 5. Why is conversation history required?

An API request does not automatically remember previous requests.

To maintain conversational context, the application sends relevant previous messages with each new request.

For example:

```text
User: What is Python?
Assistant: Python is a programming language.
User: What is it used for?
```

The application sends all three messages so the model can understand what "it" refers to.

## 6. What is the difference between an LLM and an LLM application?

- **LLM:** The underlying language model that generates responses.
- **LLM application:** The complete software system built around the model.

An LLM application may include API integration, prompt management, conversation history, validation, error handling, and a user interface.

## 7. What is a token?

A token is a unit of text processed by a language model.

A token can represent a word, part of a word, punctuation, or another text unit.

API usage and context limits are often measured in tokens.

## 8. What is a context window?

A context window is the maximum amount of input and conversation content a model can process in a single request.

It is measured in tokens and includes relevant instructions, conversation history, and current input.

## 9. How do you extract a response from the OpenAI Chat Completions API?

Example:

```python
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

content = response.choices[0].message.content
```

The first choice contains the generated assistant response.

## 10. Why should API keys be stored in environment variables?

Environment variables help keep credentials separate from application source code.

This reduces the risk of accidentally exposing secrets through source control.

## 11. How do you handle API errors?

Common errors include:

- Rate-limit or quota errors.
- Network connection errors.
- API status errors.
- Empty or invalid responses.

The application should handle expected errors and provide useful messages instead of crashing unexpectedly.

## 12. What is mocking in Python?

Mocking replaces a real dependency with a simulated object during testing.

In this project, mocked API responses allow us to test response extraction and error handling without making actual API requests.

Example:

```python
from unittest.mock import Mock

client = Mock()
client.chat.completions.create.return_value = Mock()
```

## 13. Why should an application be divided into modules?

Modular architecture separates responsibilities and makes an application easier to maintain, test, and extend.

In this project:

- `config.py` handles configuration.
- `llm_client.py` handles API communication.
- `conversation.py` manages conversation history.
- `main.py` controls the application flow.

## 14. What happens if an API request fails?

The application should handle the error gracefully, avoid adding an invalid assistant response to conversation history, and provide a useful error message.

This project removes the latest user message when the API request fails.

## 15. What improvements could be added to this project?

Possible improvements include:

- Streaming responses.
- Persistent conversation history.
- Configurable model selection.
- Retry logic with exponential backoff.
- Request timeouts.
- Logging and monitoring.
- A FastAPI interface.
- Conversation memory and database storage.

## Project Summary

Built a modular Python command-line AI assistant using the OpenAI SDK.

Implemented environment-based configuration, structured messages, conversation history, response extraction, API error handling, and mocked unit tests.

**Automated test result:** 10 passed.