import sqlite3

conn = sqlite3.connect("data/finance.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions(
id INTEGER PRIMARY KEY,
type TEXT,
amount REAL,
category TEXT,
description TEXT,
date TEXT
)
""")

conn.commit()


def add_transaction(t, amount, cat, desc, date):
    cursor.execute(
        "INSERT INTO transactions(type,amount,category,description,date) VALUES(?,?,?,?,?)",
        (t, amount, cat, desc, date)
    )
    conn.commit()


def get_transactions():
    cursor.execute("SELECT * FROM transactions")
    return cursor.fetchall()