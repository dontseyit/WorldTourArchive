# World Tour Archive

A curated archive for the races that mark the UCI World Tour calendar from the year 2020 onwards. 

The archive provides summary information about races, as well as race history, initially designed for personal use, to offer quick insights. The focus is on providing a distilled overview of each event, acknowledging that more detailed information can be found across various platforms and resources.

## Repository Structure

The repository is organized as follows:

- `races/`: This directory contains JSON files, each representing a summary of individual races. The filename convention is `<race_name>.json`.
- `src/`: Contains Python scripts utilized for data validation and processing.
  - `models.py`: Defines Pydantic models for data validation against the JSON schema.
  - `validations.py`: Contains scripts for validating race data files against the defined Pydantic models.
- `RaceSchema.json`: The JSON schema file against which race data is validated, ensuring consistency and structure across the archive.
- `requirements.txt`: Lists all Python package dependencies necessary to run the validation and processing scripts.

## Work In Progress

The World Tour Archive is a work in progress (WIP), and project scope may change in the future.

## License
This project is open-sourced under MIT License, allowing for free use, modification, and distribution with proper attribution.