import sqlite3

def main():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    # Q1. Display the names of students whose scores are greater than or equal to 90.
    cursor.execute("SELECT name, score FROM students WHERE score >= ?", (90,),)
    print("Scores greater than or equal to 90:")
    print(cursor.fetchall())

    # Q2. Display all students sorted by age, from youngest to oldest
    cursor.execute("SELECT * FROM students ORDER BY age")
    print("\nStudents sorted by age:")
    print(cursor.fetchall())

    # Q3. Display the highest score using SQL's MAX() function.
    cursor.execute("SELECT MAX(score) FROM students")
    print("\nMaximum Score:")
    print(cursor.fetchall())

    cursor.close()
    connection.close()

if __name__=='__main__':
    main()