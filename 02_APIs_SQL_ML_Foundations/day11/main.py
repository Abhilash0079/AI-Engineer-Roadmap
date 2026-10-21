import sqlite3

def main():
    connection  = sqlite3.connect("students.db")
    print("Database connected successfully.")
    
    connection.close()
    print("Database connection closed.")

if __name__=='__main__':
    main()