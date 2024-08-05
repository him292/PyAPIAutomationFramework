# Test Stack
- Python 3.12
- Requests - HTTP Requests
- Pytest
- Reporting - Allure, Pytest HTML
- Test Data - CSV, Excel, JSON, Faker
- Parallel execution - x distribute (sdist)
- Adbvance API Test case - JSON test cases

## To install all the above libraries at once, run below query:
pip install requests pytest pytest-html faker pytest-x-dist allure-pytest jsonschema 

Faker is a python library that is used to generate fake data for testing

# to run a test case
pytest tests/crud/test_create_booking.py --alluredir=allure_result -s

# how to clean the allure-reports
allure generate -clean