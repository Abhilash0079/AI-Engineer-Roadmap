import sqlite3

def main():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    # Query 1: Retrieve all records
    cursor.execute("SELECT * FROM students")
    print("All Students:")
    print(cursor.fetchall())

    # Query 2: Retrieve only names and records
    cursor.execute("SELECT name, score FROM students")
    print("\nStudent names and scores:")
    print(cursor.fetchall())

    # Query 3: Find students scoring above 85
    cursor.execute("SELECT * FROM students WHERE score > ?", (85,),)
    print("\nStudents scoring above 85:")
    print(cursor.fetchall())

    # Query 4: Sort students by score from highest to lowest
    cursor.execute("SELECT * FROM students ORDER BY score DESC")
    print("\nStudents sorted by score:")
    print(cursor.fetchall())

    # Query 5: Retrieve top 3 elements
    cursor.execute("SELECT * FROM students ORDER BY score DESC LIMIT 3")
    print("\nTop 3 Elements:")
    print(cursor.fetchall())

    cursor.close()
    connection.close()

if __name__=='__main__':
    main()