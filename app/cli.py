import click
import sqlite3
from typing import Optional
from text_processor import process_text
from word_processor import process_words_file, create_table
from config import DB_NAME


def create_database_connection(db_name: str) -> sqlite3.Connection:
    return sqlite3.connect(db_name)


def fill_database(file_path: str) -> None:
    try:
        with create_database_connection(DB_NAME) as conn:
            cursor = conn.cursor()
            create_table(cursor)
            words_added = process_words_file(file_path, cursor)
            conn.commit()
        print(f"Added {words_added} words to the database.")
    except Exception as e:
        print(f"Error while filling the database: {e}")


def process_input_text(text: Optional[str] = None, max_attempts: int = 2) -> None:
    attempts = max_attempts
    while attempts > 0:
        if text is None:
            text = input("Input: ")
        try:
            process_text(text)
            break
        except ValueError as e:
            print(f"Error: {e}")
            text = None
            attempts -= 1
    else:
        print(f"The number of attempts ({max_attempts}) has been exceeded.")


@click.command()
@click.argument('text', required=False)
@click.option('--file', type=click.Path(exists=True), help="Text file with words.")
@click.option('--fill', is_flag=True, help='Fill the database with words from the file.')
def cli(text: Optional[str], file: Optional[str], fill: bool) -> None:
    if fill:
        if not file:
            print("You must specify a file when using --fill.")
            return
        fill_database(file)
        return

    if file:
        with open(file, 'r') as f:
            text = f.read()

    process_input_text(text)


if __name__ == "__main__":
    cli()
