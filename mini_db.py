import sqlite3

class StudentDB:
    def __init__(self, db_name="campus.db"):
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS Students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    gpa REAL NOT NULL
                )
            ''')
            conn.commit()

    def add_student(self, name, gpa):
        # Using context manager for automatic closing
        with sqlite3.connect(self.db_name) as conn:
            conn.execute("INSERT INTO Students (name, gpa) VALUES (?, ?)", (name, gpa))
            conn.commit()

    def get_honors_list(self, min_gpa=3.0):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.execute("SELECT name, gpa FROM Students WHERE gpa > ?", (min_gpa,))
            return cursor.fetchall()

def main():
    db = StudentDB()
    
    # Simulate adding records
    db.add_student("Keleab", 3.9)
    db.add_student("Hagos", 2.8)
    db.add_student("Selam", 3.5)

    print("\n--- Professional Student DB ---")
    honors = db.get_honors_list(3.0)
    for name, gpa in honors:
        print(f"Honor Student: {name:10} | GPA: {gpa}")

if __name__ == "__main__":
    main()