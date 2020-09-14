from sqlite3 import Cursor

import sys; sys.path.append("..")
from src.store import get_database_cursor


def create_table(cursor: Cursor) -> None:
    cursor.execute("""CREATE TABLE summaries
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                          summary TEXT)""")
    cursor.connection.commit()


def create_database() -> None:
    cursor = get_database_cursor()
    create_table(cursor)
    cursor.connection.close()


if __name__ == '__main__':
    create_database()
