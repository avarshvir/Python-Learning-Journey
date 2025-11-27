import sqlite3

def get_conn():
    try:
        return sqlite3.connect("contacts.db", check_same_thread=False)
    except Exception as e:
        print("Connection Error:", e)

def create_table():
    try:
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT
        );
        """)
        conn.commit()
        conn.close()
    except Exception as e:
        print("Error creating table:", e)

def add_contact(name, phone):
    try:
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contacts (name, phone) VALUES (?, ?)", (name, phone))
        conn.commit()
        conn.close()
    except Exception as e:
        print("Error adding contact:", e)

def get_contacts():
    try:
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contacts")
        rows = cursor.fetchall()
        conn.close()
        return rows
    except Exception as e:
        print("Error fetching data:", e)

def delete_contact(contact_id):
    try:
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
        conn.commit()
        conn.close()
    except Exception as e:
        print("Error deleting:", e)
