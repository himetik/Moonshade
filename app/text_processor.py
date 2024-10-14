from text_validator import validate_text


def process_text(text):
    try:
        validate_text(text)
        print("Ok")

    except ValueError as e:
        print(f"Validation error: {e}")
