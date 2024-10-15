import re
from typing import List
from config import MAX_OUTPUT_LINES
from abbreviations import abbreviations


def split_text_into_sentences(text: str, max_output_lines: int = MAX_OUTPUT_LINES) -> List[str]:
    text = re.sub(r'\s+', ' ', text)

    abbr_patterns = [re.compile(rf'{re.escape(abbr)}$') for abbr in abbreviations]
    split_pattern = re.compile(r'(?<=[.!?]) +')

    potential_sentences = split_pattern.split(text.strip())
    merged_sentences = []
    buffer = ""

    for sentence in potential_sentences:
        if any(pattern.search(sentence) for pattern in abbr_patterns):
            buffer += sentence + " "
        else:
            if buffer:
                merged_sentences.append(buffer + sentence)
                buffer = ""
            else:
                merged_sentences.append(sentence)

    if buffer:
        merged_sentences.append(buffer.strip())

    merged_sentences = [re.sub(r'\s+', ' ', sentence).strip() for sentence in merged_sentences]

    return merged_sentences[:max_output_lines]
