import json
import logging

logging.basicConfig(
    filename="validator.log",
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    filemode="a",
    encoding="utf-8"
)

def load_students(file_path: str) -> list:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

    except FileNotFoundError:
        logging.error("Input file not found: %s", file_path)
        print("Error: Student records file was not found.")
        return []

    except json.JSONDecodeError:
        logging.error("Invalid JSON in file: %s", file_path)
        print("Error: Student records file contains invalid JSON.")
        return []

    if not isinstance(data, dict) or not isinstance(data.get("students"), list):
        logging.error("Invalid JSON structure in file: %s", file_path)
        print("Error: Expected a JSON object containing a students list.")
        return []

    logging.info("Loaded %d student records.", len(data["students"]))
    return data["students"]


def validate_students(students: list) -> list:
    valid_students = []

    for student in students:
        if not isinstance(student, dict):
            logging.warning("Rejected record: Expected a dictionary.")
            continue

        name = student.get("name")
        score = student.get("score")

        if not isinstance(name, str) or not name.strip():
            logging.warning("Rejected record: Student name is missing or empty.")
            continue

        if (
            not isinstance(score, (int, float))
            or isinstance(score, bool)
        ):
            logging.warning("Rejected record for %s: Score must be numeric.", name)
            continue

        valid_students.append(student)

    logging.info(
        "Validation complete: %d valid record(s) out of %d.",
        len(valid_students),
        len(students)
    )
    return valid_students


if __name__ == "__main__":
    students = load_students("students_records.json")
    valid_students = validate_students(students)

    print(f"Valid records: {len(valid_students)}")

    for student in valid_students:
        print(student)
