import sqlite3

def run_db_test():
    # Connect to a local file (creates it if missing)
    conn = sqlite3.connect('campus.db')
    cursor = conn.cursor()

    # 1. Create the table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            gpa REAL
        )
    ''')

    # 2. Clear old data for a clean test
    cursor.execute('DELETE FROM Students')

    # 3. Insert 3 students using placeholders (?) for security
    student_data = [
        ('Abebe', 3.8),
        ('Sara', 2.9),
        ('John', 3.5)
    ]
    cursor.executemany('INSERT INTO Students (name, gpa) VALUES (?, ?)', student_data)
    
    conn.commit()

    # 4. Select students with GPA > 3.0
    print("--- Students with GPA > 3.0 ---")
    cursor.execute('SELECT name, gpa FROM Students WHERE gpa > 3.0')
    
    for row in cursor.fetchall():
        print(f"Name: {row[0]} | GPA: {row[1]}")

    conn.close()

if __name__ == "__main__":
    run_db_test()
    