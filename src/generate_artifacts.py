import csv
from pathlib import Path
from models import Race
from validations import validate_all

# Define your CSV file path
CSV_FILE_PATH = "races.csv"


def write_to_csv():
    """Write all race information to a CSV file"""
    race_files = Path("./races").glob("**/*.json")
    with open(CSV_FILE_PATH, mode="w", newline="", encoding="utf-8") as file:
        # Write the header
        fieldnames = list(Race.model_fields.keys())
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for path in race_files:
            with open(str(path), "r", encoding="utf-8") as f:
                json_str = f.read()

            race_instance = Race.model_validate_json(json_str)
            writer.writerow(race_instance.model_dump())

        print(f"Races have been written to {CSV_FILE_PATH}")


# Validate all JSON files
validate_all()

# Write all to CSV
write_to_csv()
