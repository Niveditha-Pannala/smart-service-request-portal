from database import cursor, conn

cursor.execute("""
CREATE TABLE IF NOT EXISTS requests (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    category TEXT,
    description TEXT,
    priority TEXT,
    name TEXT,
    email TEXT,
    status TEXT

)
""")

conn.commit()