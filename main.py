from utils.greetings import greet_user

def greet_user(name):
    """Return a greeting for the given user."""
    return f"Hello, {name}! Welcome to AI Engineering."


def calculate_total(first_number, second_number):
    """Return the sum of two numbers."""
    return first_number + second_number


user_message = greet_user("Abhilash")
total = calculate_total(10, 20)

print(user_message)
print(f"The total is: {total}")

print(greet_user("Abhilash"))