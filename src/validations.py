from pydantic import ValidationError
from models import Race
from pathlib import Path

def validate_all():
    """Validate all race files and return the validation information"""
    validation_results = []
    race_files = Path("./races").glob('**/*.json')
    for path in race_files:
        with open(str(path), 'r', encoding="utf-8") as f:
            json_str = f.read()

            try:
                Race.model_validate_json(json_str)
            except ValidationError as e:
                validation_results.append(f"ERROR: {str(path.name)}: {e.json()}")
            else:
                validation_results.append(f"INFO: {str(path.name)}: validated")
            
    for validation in validation_results:
        print(validation)
    
    return validation_results
