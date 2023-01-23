import sqlite3
import textwrap

connection = sqlite3.connect('database.db')


sqlCommand = """
    CREATE TABLE IF NOT EXISTS posts ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item TEXT
    );

    INSERT INTO posts (item) VALUES(
        'Esempio'
    );
"""
sqlCommand = textwrap.indent(sqlCommand, '  ')





connection.executescript(sqlCommand)
connection.commit()
connection.close()