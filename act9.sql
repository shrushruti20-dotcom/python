import sqlite3
connection = sqlite3.connect("database2.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE student(
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")
cursor.execute("""
INSERT INTO student(name,age)
VALUES
('Rahul',11),
('Anananya',12),
('arjun',11)
""")
connection.commit()
connection.close()
print("database2.db created successfully")
