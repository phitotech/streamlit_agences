
import sqlite3
from datetime import datetime

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sources (
    id INTEGER PRIMARY KEY,
    nom TEXT,
    type TEXT,
    region TEXT,
    theme TEXT,
    url TEXT,
    date_collecte TEXT
)
""")

cursor.execute("""
INSERT INTO sources (nom, type, region, theme, url, date_collecte)
VALUES (?, ?, ?, ?, ?, ?)
""", ("UNESCO", "ONU", "Afrique", "Éducation", "https://unesco.org", datetime.now().isoformat()))

conn.commit()
conn.close()
