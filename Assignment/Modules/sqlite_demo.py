import sqlite3

connection = sqlite3.connect(
    r"C:\PYTHON\Assignment\Modules\students.db"
)

print("Database connected successfully!")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")
cursor.execute("""
INSERT INTO students (name, age, course)
VALUES ('Rahul', 21, 'BTech')
""")

cursor.execute("""
INSERT INTO students (name, age, course)
VALUES ('Amit', 22, 'MBA')
""")

cursor.execute("""
INSERT INTO students (name, age, course)
VALUES ('Priya', 20, 'CA')
""")

connection.commit()

connection.commit()

print("Table created successfully!")

connection.close()

print("Database closed!")