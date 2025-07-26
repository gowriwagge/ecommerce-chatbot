import sqlite3

def init_db():
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_to_db(question, answer):
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute('INSERT INTO chat_history (question, answer) VALUES (?, ?)', (question, answer))
    conn.commit()
    conn.close()

def fetch_answer(question):
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute('SELECT answer FROM chat_history WHERE question = ?', (question,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None
