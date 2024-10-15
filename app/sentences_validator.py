import re
from config import MAX_SENTENCE_LENGTH, MIN_SENTENCE_LENGTH


def is_not_empty(sentence):
    return bool(sentence and sentence.strip())


def starts_with_uppercase(sentence):
    return sentence[0].isupper() if sentence else False


def ends_with_punctuation(sentence: str) -> bool:
    if not sentence:
        return False

    pattern = r'\S[.!?]$'

    return bool(re.search(pattern, sentence.strip()))

def has_text_before_punctuation(sentence: str) -> bool:
    if not sentence:
        return False

    pattern = r'\S+[.!?]$'

    return bool(re.search(pattern, sentence.strip()))


def has_no_extra_spaces(sentence):
    return '  ' not in sentence and '\n' not in sentence


def is_within_length_limits(sentence):
    return MIN_SENTENCE_LENGTH <= len(sentence) <= MAX_SENTENCE_LENGTH


def contains_valid_characters(sentence):
    return bool(re.match(r'^[A-Za-z0-9.,!?\'":; \-]+$', sentence))


def is_single_word(sentence):
    return len(sentence.split()) == 1


def validate_sentence(sentence):
    if not is_not_empty(sentence): return False
    if is_single_word(sentence): return False
    if not starts_with_uppercase(sentence): return False
    if not ends_with_punctuation(sentence): return False
    if not has_no_extra_spaces(sentence): return False
    if not is_within_length_limits(sentence): return False
    if not contains_valid_characters(sentence): return False
    return True


def filter_valid_sentences(sentences):
    return [sentence for sentence in sentences if validate_sentence(sentence)]
