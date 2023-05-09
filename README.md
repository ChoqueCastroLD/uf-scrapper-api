# UF API

## Overview
This project provides an API for retrieving the value of the UF (Unidad de Fomento) for a specific date. The API fetches the data from an external source and returns it in JSON format.

## Installation
1. Clone the repository: `git clone https://github.com/your-username/uf-api.git`
2. Navigate to the project directory: `cd uf-api`
3. Create and activate a virtual environment (optional but recommended): 
   - For virtualenv: `python -m venv venv` and then `source venv/bin/activate`
   - For pipenv: `pipenv install` and then `pipenv shell`
4. Install the dependencies: `pip install -r requirements.txt`

## Quick Usage
1. Install Dependecies `pip install -r requirements.txt`
2. Run `python .\main.py`

## Venv & Flask Usage
1. Start the Flask development server:
   - For virtualenv: `python api/app.py`
   - For pipenv: `pipenv run python api/app.py`
2. The API will be accessible at `http://localhost:5000`
3. To retrieve the UF value for a specific date, send a GET request to `/uf` with the `date` parameter in the format `dd-mm-yyyy`. Example: `http://localhost:5000/uf?date=10-05-2023`

## API Endpoints

### Get UF Value
- URL: `/uf`
- Method: GET
- Query Parameters:
  - `date`: The date for which to retrieve the UF value (format: dd-mm-yyyy)
- Response: JSON object with the following structure:
 ```json
  {
    "date": "10-05-2023",
    "value": 1234.56
  }
```

## Running Tests
1. Unit Tests:
   - python -m unittest discover tests/unit
   - For virtualenv: `python -m unittest discover tests/unit`
   - For pipenv: `pipenv run python -m unittest discover tests/unit`

## Project Structure
The project follows a modular structure for better organization and separation of concerns. Here's an overview of the project structure:

- `api`: Contains the main API application code.
  - `uf`: Handles the UF-related functionality.
    - `uf_controller.py`: Defines the UF API endpoints and request handling.
    - `uf_service.py`: Implements the UF service for fetching UF values.
    - `uf_repository.py`: Handles data retrieval from external sources.
  - `error_handling`: Handles API error handling and custom exceptions.
    - `error_handler.py`: Defines the error handling logic.
    - `errors.py`: Contains custom error classes for different HTTP status codes.
  - `util`: Contains utility functions used in the API.
    - `parse_date.py`: Implements date parsing and validation functions.

- `tests`: Contains unit tests for the API.
  - `unit`: Contains unit tests for individual modules and functions.

- `__init__.py`: Initializes the Flask application and registers blueprints.
