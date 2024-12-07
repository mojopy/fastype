# data_manager.py

import json
from constants import HIGH_SCORES_FILE, LAST_LEVEL_FILE

def load_words(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def save_high_scores(high_scores):
    with open(HIGH_SCORES_FILE, "w") as f:
        for score in high_scores[:10]:  # Keep only the top 10 scores
            f.write(f"{score}\n")

def load_high_scores():
    try:
        with open(HIGH_SCORES_FILE, "r") as f:
            return [int(line.strip()) for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_last_level(level):
    with open(LAST_LEVEL_FILE, "w") as f:
        f.write(level)

def load_last_level():
    try:
        with open(LAST_LEVEL_FILE, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None
