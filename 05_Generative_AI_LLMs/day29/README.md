# Day 29 — LLM APIs: Command-Line AI Assistant

## Project Overview

A modular Python command-line AI assistant that demonstrates how a Python application communicates with a Large Language Model (LLM) through an API.

The application manages conversation history, loads configuration securely through environment variables, sends messages to the OpenAI API, and handles common API errors.

**Note:** The project currently uses mocked API responses for testing. A real API key is not required to run the test suite.

## Learning Objectives

- Understand how LLM APIs work.
- Understand API keys and environment variables.
- Structure chat messages using system, user, and assistant roles.
- Maintain conversation history.
- Send requests through the OpenAI Python SDK.
- Extract generated responses.
- Handle API connection, rate-limit, and empty-response errors.
- Write unit tests using Python mocks.

## Project Structure

```text
day29/
│
├── .env.example
├── config.py
├── conversation.py
├── llm_client.py
├── main.py
├── README.md
├── INTERVIEW_NOTES.md
│
└── tests/
    ├── test_config.py
    ├── test_conversation.py
    └── test_llm_client.py
```

The project uses the shared virtual environment and root-level `requirements.txt` from the AI Engineer roadmap repository.

## Technologies

- Python
- OpenAI Python SDK
- python-dotenv
- pytest
- unittest.mock

## Setup

### 1. Activate the virtual environment

From the roadmap root directory:

```powershell
.\venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 3. Configure environment variables

The `.env.example` file contains a placeholder:

```text
OPENAI_API_KEY=your_api_key_here
```

If you want to make a real API request, create a local `.env` file in the project directory and configure your own API key.

Never commit `.env` or expose API keys in source code.

A real API request may incur charges depending on API usage and account billing.

## Running the Tests

From the Day 29 project directory:

```powershell
python -m pytest tests -v
```

The project currently contains 10 tests covering:

- Configuration loading and missing API key validation.
- Conversation initialization and message management.
- Successful response extraction.
- Empty response validation.
- Rate-limit error handling.
- API connection error handling.

**Latest test result:** 10 passed.

## Running the Application

After configuring a valid API key and confirming access to the selected model:

```powershell
python main.py
```

The application starts an interactive command-line session.

- Enter a message to communicate with the assistant.
- Enter `exit` to close the application.

## Application Modules

| Module | Responsibility |
|---|---|
| `config.py` | Loads and validates environment configuration. |
| `llm_client.py` | Creates the OpenAI client and generates responses. |
| `conversation.py` | Initializes and manages conversation history. |
| `main.py` | Runs the command-line assistant. |
| `tests/` | Contains automated unit tests. |

## Important Concepts

- **LLM:** A Large Language Model that generates responses based on input.
- **API:** An interface that allows applications to communicate with external services.
- **API key:** A credential used to authenticate API requests.
- **Messages:** Structured conversation entries containing a role and content.
- **Conversation history:** Previous messages sent again as context for subsequent requests.
- **Tokens:** Units of text processed by a language model.
- **Mocking:** Simulating external dependencies so code can be tested without making real API calls.

## Current Limitations

- The project currently integrates with the OpenAI Chat Completions interface.
- Live API requests have not yet been tested.
- The application uses an in-memory conversation history, which is lost when the program exits.
- No database or persistent conversation storage is implemented.

## Learning Outcome

Built a modular command-line AI assistant and tested its configuration, conversation management, response extraction, and API error handling without requiring a live API key.