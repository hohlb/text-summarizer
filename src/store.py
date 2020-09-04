import sqlite3
from typing import Union


def store_text(long_text: str) -> Union[int, None]:
    """Store the given long text into the database and return the resulting row ID."""
    conn = sqlite3.connect('summaries.db')
    row_id = None

    with conn:
        cursor = conn.cursor()
        parameters = (long_text,)
        cursor.execute("INSERT INTO summaries(long_text) values (?)", parameters)
        row_id = cursor.lastrowid

    conn.close()
    
    return row_id
