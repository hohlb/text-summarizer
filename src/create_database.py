import sqlite3

conn = sqlite3.connect('summaries.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE summaries
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                      summary TEXT)''')

conn.commit()
conn.close()
