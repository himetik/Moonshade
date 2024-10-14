from text_validator import validate_text
from text_splitter import split_text_into_sentences
from sentences_validator import filter_valid_sentences


def process_text(text):
    try:
        validate_text(text)

        sentences = split_text_into_sentences(text)
        valid_sentences = filter_valid_sentences(sentences)

        if not valid_sentences:
            print("Valid sentences not found.")
            return

        for sentence in valid_sentences:
            print(sentence)

    except ValueError as e:
        print(f"Validation error: {e}")
