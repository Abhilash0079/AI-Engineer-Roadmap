import json

try:
    with open('students.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    for student in data['students']:
        print(f"Name: {student['name']}, Score: {student['score']}")

except FileNotFoundError:
    print("Invalid file name. File may not exists.")