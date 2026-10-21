import sqlite3

def main():
    connection  = sqlite3.connect("students.db")
    cursor = connection.cursor()
    
    #Create the table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            score REAL
        )
    """)

    connection.commit()
    print("Student table created successfully.")

    cursor.close()
    connection.close()
    print("Database connection closed.")
    
    if __name__=='__main__':
        main()