import csv
from pathlib import Path


def load_search_cases():
    csv_path = Path(__file__).resolve().parents[1] / "data" / "search_cases.csv"

    with csv_path.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))