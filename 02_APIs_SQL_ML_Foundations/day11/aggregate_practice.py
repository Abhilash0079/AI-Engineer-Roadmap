import sqlite3

def main():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    # Query 6: Count total number of students
    cursor.execute("SELECT COUNT(*) FROM students")
    print("Count of Students:")
    print(cursor.fetchone())

    # Queery 7: Calculate sum of all student scores
    cursor.execute("SELECT SUM(score) FROM students")
    print("\nSum of score:")
    print(cursor.fetchone())

    # Query 8: Calculate the average score
    cursor.execute("SELECT AVG(score) FROM students")
    print("\nAverage Score:")
    print(cursor.fetchone())

    cursor.close()
    connection.close()

if __name__=='__main__':
    main()
