import re
from typing import List
from config import MAX_OUTPUT_LINES


abbreviations = [
    r"Mr\.", r"Mrs\.", r"Ms\.", r"Dr\.", r"Prof\.", r"Rev\.",
    r"Hon\.", r"Sr\.", r"Jr\.", r"Esq\.",

    r"etc\.", r"i\.e\.", r"e\.g\.", r"viz\.", r"vs\.", r"ca\.",
    r"cf\.", r"N\.B\.", r"P\.S\.", r"Q\.E\.D\.",

    r"Ph\.D\.", r"M\.D\.", r"B\.A\.", r"M\.A\.", r"B\.Sc\.", r"M\.Sc\.",
    r"LL\.B\.", r"J\.D\.", r"M\.B\.A\.",

    r"a\.m\.", r"p\.m\.", r"A\.D\.", r"B\.C\.", r"B\.C\.E\.", r"C\.E\.",

    r"Ave\.", r"Blvd\.", r"St\.", r"Rd\.", r"Mt\.", r"Ft\.",

    r"Inc\.", r"Ltd\.", r"Corp\.", r"Co\.", r"LLC\.",

    r"Gen\.", r"Col\.", r"Maj\.", r"Capt\.", r"Lt\.", r"Sgt\.",

    r"kg\.", r"cm\.", r"mm\.", r"km\.", r"ft\.", r"in\.", r"lbs\.",

    r"www\.", r"http\.", r"https\.", r"ftp\.", r"HTML\.", r"CSS\.", r"JS\.",

    r"approx\.", r"dept\.", r"est\.", r"fig\.", r"vol\.", r"no\.",
    r"pp\.", r"sec\.", r"min\.", r"hr\.", r"pts\.", r"oz\.",

    r"Sr\.", r"Sra\.", r"Srta\.",
    r"M\.", r"Mme\.", r"Mlle\.",
    r"Herr\.", r"Fr\.", r"Frl\.",
]


def split_text_into_sentences(text: str, max_output_lines: int = 100) -> List[str]:
    split_pattern = re.compile(r'(?<=[.!?]) +')

    abbr_patterns = [re.compile(f'{abbr}$') for abbr in abbreviations]

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

    return merged_sentences[:max_output_lines]
