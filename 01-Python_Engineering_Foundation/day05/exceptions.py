"""
Exception handling
An exception is an error condition that occurs while a program runs. We use try and except to handle expected errors without letting them become unhandled failures.

For example, consider an AI application that receives a number from a user. The user might enter text instead of a number.
"""

user_input  = "abdc"
# number = int(user_input)
# print(number)

try:
    number = int(user_input)
    print(number)
except ValueError:
    print("Invalid input: Please enter a valid integer.")


"""
Interview tip: Catch specific exceptions such as ValueError when you know which failure you're handling. Avoid catching every exception indiscriminately with a broad except, because it can hide unexpected bugs.
"""