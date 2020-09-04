import sqlite3
from typing import Union


def create_summary_id() -> Union[int, None]:
    """Create a new database entry in which the summary will be stored and return the row ID."""
    conn = sqlite3.connect("summaries.db")
    row_id = None

    with conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO summaries(summary) values (NULL)")
        # the actual summary will be filled in shortly via a background task

        row_id = cursor.lastrowid

    conn.close()
    
    return row_id


def save_summary(summary: str, document_id: int) -> None:
    """Save the summary into the database under the given ID."""
    conn = sqlite3.connect("summaries.db")

    with conn:
        cursor = conn.cursor()
        parameters = (summary, document_id)
        cursor.execute("UPDATE summaries SET summary = ? WHERE id = ?", parameters)

    conn.close()


def get_summary(document_id: int) -> Union[str, None]:
    """Get the summary from the database via the given ID."""
    conn = sqlite3.connect("summaries.db")
    summary = None

    with conn:
        cursor = conn.cursor()
        parameters = (document_id,)
        cursor.execute("SELECT summary FROM summaries WHERE id = ?", parameters)
        summary = cursor.fetchone()[0]

    conn.close()

    return summary
