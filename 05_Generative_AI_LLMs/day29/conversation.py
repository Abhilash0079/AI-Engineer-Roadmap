def create_conversation():
    """Initialize conversation with system instructions."""
    return [
        {
            "role": "system",
            "content": "You are a helpful AI assistant. "
                        "Provide clear and accurate answers."
        }
    ]

def add_user_message(message, content):
    """Add a user message to conversation history."""
    message.append({
        "role": "user",
        "content": content
    })

def add_assistant_message(messages, content):
    """Add an assistant response to conversation history."""
    messages.append({
        "role": "assistant",
        "content": content
    })