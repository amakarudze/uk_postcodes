# uk_postcodes
A library for formatting and validating UK postcodes.

## Installation

### Requirements
* Python 3.7+
* Django
* [Code-Point Open](https://www.ordnancesurvey.co.uk/business-government/products/code-point-open) UK postcode data.

### Installing
* Clone the repo.
* Create and activate a virtual environment and run ```pip install -r requirements.txt```.
* Download the 1.7 million current UK postcodes from [Code-Point Open](https://www.ordnancesurvey.co.uk/business-government/products/code-point-open) for testing.

### Running Tests
To run tests, run ```python manage.py test```.

## Usage
To use this api send a request with the postcode you want to format and validate to this url: 
```http://127.0.0.1:8000/<postcode>```

## Contributing
To contribute to this library, please read our [contributing guide here](Contributing.md).
