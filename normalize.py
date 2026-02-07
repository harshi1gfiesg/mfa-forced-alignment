import re
from pathlib import Path
from num2words import num2words

DATA_DIR = Path("data/speaker1")


def normalize_line(line):
    line = line.upper()

    # Convert numbers to words
    def replace_number(match):
        return num2words(int(match.group())).upper()

    line = re.sub(r"\b\d+\b", replace_number, line)

    # Replace hyphens with space
    line = line.replace("-", " ")

    # Remove punctuation (keep letters & spaces)
    line = re.sub(r"[^A-Z\s]", " ", line)

    # Normalize whitespace
    line = re.sub(r"\s+", " ", line).strip()

    return line


def normalize_file(path):
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    normalized = [normalize_line(l) for l in lines if l.strip()]
    path.write_text("\n".join(normalized), encoding="utf-8")


if __name__ == "__main__":
    for txt_file in DATA_DIR.glob("*.txt"):
        normalize_file(txt_file)
        print(f"Normalized: {txt_file.name}")
