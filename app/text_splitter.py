import re
from config import MAX_OUTPUT_LINES


def split_text_into_sentences(text):
    sentences = re.split(r'(?<=[.!?]) +', text.strip())

    return sentences[:MAX_OUTPUT_LINES]
