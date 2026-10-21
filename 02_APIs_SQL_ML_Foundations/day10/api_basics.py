"""
Understand APIs, HTTP, and JSON

- What is an API?
An API (Application Programming Interface) allows two software applications to communicate with each other.

For example, imagine you're building a cricket analytics application. Your Python application needs the latest match scores from a cricket data service.
                        Your Python application
                    Requests the latest match score
                                    |
                        HTTP request and response
                                    |
                        External API server
                                    |
                    Processes the request and returns data


Your application sends a request. The server processes it and returns a response, often containing JSON data.

- Learn the three important concepts:

HTTP — How applications communicate
HTTP defines how clients send requests and servers return responses.

Common methods include:
- GET — retrieve data.
- POST — submit or create data.
- PUT — replace an existing resource.
- DELETE — delete a resource.

JSON — A format for exchanging data
JSON represents structured data using objects, arrays, strings, numbers, booleans, and null values.

Example:
{
  "player": "Virat Kohli",
  "runs": 82,
  "not_out": true
}

HTTP status codes — The result of a request
Code	    Meaning
200	    Request succeeded
201	    Resource created
400	    Bad request
401	    Authentication required or failed
404	    Resource not found
500	    Server error

"""
import json

# match = {
#     "team" : "India",
#     "opponent" : "Australia",
#     "runs" : 285,
#     "wickets" : 6,
#     "won" : True
# }

# # Convert the Python dictionary to a JSON string
# json_data = json.dumps(match, indent=4)

# print("JSON Data:")
# print(json_data)

# # Convert JSON String back to Python Dictionary
# match_data = json.loads(json_data)

# print("\nPython Data: ")
# print(match_data)

# print("\nTeam:", match_data["team"])
# print("Runs:", match_data["runs"])

"""
- Make your first HTTP GET request
Now we'll use an actual API over the internet.
We'll use JSONPlaceholder — a free testing API that returns sample JSON data. Its /posts/1 endpoint returns a sample post.

"""

# Send your first GET request
import requests

# print("\n----- Making an HTTP GET request -----")
# url = "https://jsonplaceholder.typicode.com/posts/1"

# response = requests.get(url, timeout=10)

# print("Status code:", response.status_code)
# print("Response successful: ", response.ok)

# print("\nResponse JSON:")
# print(response.json())

# print("\nPost title:")
# print(response.json()["title"])

"""
- Handle HTTP errors safely
A successful request is only half the job. In real AI applications, APIs can return errors, network connections can fail, or a server can take too long to respond.
"""
def fetch_post(post_id: int) -> None:
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    try:
        response = requests.get(url, timeout=10)
        print("\nStatus code:", response.status_code)
        response.raise_for_status()
        post = response.json()
        print("Post title:", post["title"])

    except requests.exceptions.Timeout:
        print("Error: The request timed out.")

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API.")

    except requests.exceptions.HTTPError as error:
        print("HTTP error:", error)


print("\n--- Testing a Valid Post ---")
fetch_post(1)

print("\n--- Testing a Missing Post ---")
fetch_post(1000)