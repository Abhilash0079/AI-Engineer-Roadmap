from conversation import (
    create_conversation,
    add_user_message,
    add_assistant_message
)

def test_create_conversation():
    messages = create_conversation()

    assert len(messages) == 1
    assert messages[0]['role'] == "system"

def test_add_user_message():
    messages = create_conversation()

    add_user_message(messages, "What is Python?")

    assert messages[-1]['role'] == "user"
    assert messages[-1]['content'] == "What is Python?"

def test_add_assistant_message():
    messages = create_conversation()

    add_assistant_message(messages, "Python is a programming language.")

    assert messages[-1]['role'] == "assistant"
    assert messages[-1]['content'] == "Python is a programming language."

def test_conversation_history():
    messages = create_conversation()

    add_user_message(messages, "What is Python?")
    add_assistant_message(messages, "Python is a programming language.")
    add_user_message(messages, "What is it used for?")

    assert len(messages) == 4
    assert messages[1]['role'] == 'user'
    assert messages[2]['role'] == 'assistant'
    assert messages[3]['role'] == 'user'