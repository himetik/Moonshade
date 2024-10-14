from text_validator import validate_text
from text_splitter import split_text_into_sentences


def process_text(text):
    try:
        validate_text(text)
        print("Ok")

        split_text_into_sentences(text)

    except ValueError as e:
        print(f"Validation error: {e}")
