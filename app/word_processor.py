import sqlite3
import os
import re
from config import DB_NAME, TABLE_NAME, BATCH_SIZE


def create_database(DB_NAME: str) -> sqlite3.Connection:
    if not os.path.exists(DB_NAME):
        pass
    try:
        conn = sqlite3.connect(DB_NAME)
        return conn
    except sqlite3.DatabaseError as e:
        raise Exception(f"Failed to connect to the database: {e}")


def create_table(cursor: sqlite3.Cursor):
    try:
        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        id INTEGER PRIMARY KEY,
        word TEXT UNIQUE
        )
        ''')
    except sqlite3.DatabaseError as e:
        raise Exception(f"Error creating table '{TABLE_NAME}': {e}")


def validate_word(word: str) -> bool:
    return bool(re.match(r'^[a-zA-Z-]{2,59}$', word))


def insert_words(cursor: sqlite3.Cursor, words: list) -> int:
    try:
        valid_words = []
        for word in words:
            if validate_word(word):
                valid_words.append(word)

        cursor.executemany(
            f'INSERT OR IGNORE INTO {TABLE_NAME} (word) VALUES (?)',
            [(word,) for word in valid_words]
        )
        return cursor.rowcount
    except sqlite3.DatabaseError as e:
        raise Exception(f"Error inserting words into the table: {e}")


def process_words_file(file_path: str, cursor: sqlite3.Cursor) -> int:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")
    if not os.access(file_path, os.R_OK):
        raise PermissionError(f"File '{file_path}' is not readable.")

    added_words_count = 0
    try:
        with open(file_path, 'r') as file:
            words_batch = []
            for line in file:
                word = line.strip().lower()
                words_batch.append(word)
                if len(words_batch) >= BATCH_SIZE:
                    added_words_count += insert_words(cursor, words_batch)
                    words_batch.clear()
            if words_batch:
                added_words_count += insert_words(cursor, words_batch)
    except IOError as e:
        raise Exception(f"An error occurred while reading the file: {e}")

    return added_words_count


def process_file(file_path: str) -> int:
    conn = create_database(DB_NAME)
    cursor = conn.cursor()
    create_table(cursor)

    try:
        added_count = process_words_file(file_path, cursor)
        conn.commit()
        return added_count
    except Exception as e:
        conn.rollback()
        raise
    finally:
        conn.close()
