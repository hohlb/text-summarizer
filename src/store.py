from sqlite3 import connect, Cursor
from typing import Union


def create_summary_id() -> Union[int, None]:
    """Create a new database entry in which the summary will be stored and return the row ID."""
    cursor = get_database_cursor()
    cursor.execute("INSERT INTO summaries(summary) values (NULL)")
    # the actual summary will be filled in via the background task started in create_summary() in main.py

    row_id = cursor.lastrowid

    commit_and_close(cursor)
    
    return row_id


def save_summary(summary: str, document_id: int) -> None:
    """Save the summary into the database under the given ID."""
    parameters = (summary, document_id)
    cursor = get_database_cursor()    
    cursor.execute("UPDATE summaries SET summary = ? WHERE id = ?", parameters)

    commit_and_close(cursor)


def get_summary(document_id: int) -> Union[str, None]:
    """Get the summary from the database via the given ID."""
    cursor = get_database_cursor()

    parameters = (document_id,)
    cursor.execute("SELECT summary FROM summaries WHERE id = ?", parameters)
    summary = cursor.fetchone()[0]

    commit_and_close(cursor)

    return summary


def get_database_cursor() -> Cursor:
    conn = connect("summaries.db")

    return conn.cursor()


def commit_and_close(cursor: Cursor) -> None:
    cursor.connection.commit()
    cursor.connection.close()
