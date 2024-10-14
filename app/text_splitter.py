import re
from config import MAX_OUTPUT_LINES


def split_text_into_sentences(text):
    sentences = re.split(r'(?<=[.!?]) +', text.strip())

    for sentence in sentences[:MAX_OUTPUT_LINES]:
        print(sentence)

    return sentences
