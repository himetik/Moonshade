from config import MAX_TEXT_SIZE


def validate_text(text):
    if not text or not text.strip():
           raise ValueError("Text cannot be empty.")

    text_bytes = text.encode('utf-8')

    if len(text_bytes) > MAX_TEXT_SIZE:
        raise ValueError(f"Text is too large. Maximum size: {MAX_TEXT_SIZE} bytes.")
