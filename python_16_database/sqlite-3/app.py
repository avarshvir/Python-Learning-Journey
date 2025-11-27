import sqlite3

# Connect to SQLite
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
"""
connect() → creates/opens database file
cursor() → creates a cursor for executing SQL commands
"""

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")

conn.commit()

# Insert data
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Alice", 20))

conn.commit()
# (We use ? to avoid SQL injection.)

# Select (fetch) data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Delete data
cursor.execute("DELETE FROM students WHERE id = ?", (6,))
conn.commit()

# Update data
cursor.execute("UPDATE students SET age = ? WHERE id = ?", (25, 2))
conn.commit()

# Delete table
cursor.execute("""
DROP TABLE students               
""")

print("Table is deleted")
# Close connection
conn.close()
