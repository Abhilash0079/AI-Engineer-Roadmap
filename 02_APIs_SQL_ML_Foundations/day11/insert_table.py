import sqlite3

def main():
    connection  = sqlite3.connect("students.db")
    print("Database connected successfully.")
    cursor = connection.cursor()

    # Insert the values in the table.
    students = [
        (1, "Abhilash", 25, 95.0),
        (2, "Priya", 23, 85.0),
        (3, "Amit", 24, 92.0),
        (4, "Rahul", 22, 72.0),
        (5, "Neha", 26, 88.5),
    ]
    
    cursor.executemany(
        """
        INSERT OR IGNORE INTO students(id, name, age, score)
        VALUES(?,?,?,?)
        """,
        students,
    )

    connection.commit()
    print("Student records inserted successfully.")
    
    cursor.close()
    connection.close()
    print("Database connection closed.")
    
if __name__=='__main__':
    main()
    