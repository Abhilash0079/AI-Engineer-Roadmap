from config import load_config
from llm_client import create_llm_client, generate_response
from conversation import (
    create_conversation,
    add_user_message,
    add_assistant_message
)

def main():
    """Run the command-line AI assistant."""
    config = load_config()
    client = create_llm_client(config['api_key'])
    messages = create_conversation()

    print("AI Assistant")
    print("Type 'exit' to quit.")
    print("-"*40)

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "exit":
            print("Assistant: Goodbye!")
            break

        if not user_input:
            print("Assistant: Please enter a message.")
            continue

        add_user_message(messages, user_input)

        try:
            response = generate_response(client, messages)
            add_assistant_message(messages, response)
            print("\nAssistant:", response)

        except Exception as error:
            messages.pop()
            print(f"\nAPI Error: {error}")

if __name__ == "__main__":
    main()