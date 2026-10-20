import csv

try:
    with open('students.csv', 'r', encoding='utf-8', newline="") as file:
        reader = csv.DictReader(file)

        for student in reader:
            print(f"Name: {student['name']}, Score: {student['score']}")

except FileNotFoundError:
    print("Invalid file name. File may not exists.")