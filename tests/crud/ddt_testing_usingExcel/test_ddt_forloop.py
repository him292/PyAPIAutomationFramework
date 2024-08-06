# Read the Excel file
# Create a function 'create_token' which can take values from excel file and verify the expected result

import openpyxl
import requests
import allure
import pytest
from src.helpers.api_requests_wrapper import post_request


def read_credentials_from_file(file_path):
    """
    Reads username and password credentials from an Excel file.
    Args:
        file_path (str): The path to the Excel file containing the credentials.
    Returns:
        list: A list of dictionaries, where each dictionary contains a 'username' and 'password' key-value pair.
    """
    credentials = []  # Create an empty list to store the credentials

    # Load the Excel workbook
    workbook = openpyxl.load_workbook(filename=file_path)
    sheet = workbook.active  # Get the active sheet from the workbook

    # Iterate over the rows in the sheet, starting from the second row
    for row in sheet.iter_rows(min_row=2, values_only=True):
        # Unpack the username and password from the current row
        username, password = row
        # Create a dictionary with the username and password
        # Add the dictionary to the credentials list
        credentials.append(({
            "username": username,
            "password": password
        }))

    return credentials


def create_auth_req(username, password):
    payload = {
        "username": username,
        "password": password
    }
    response = post_request
    return response


def test_create_auth_request_with_Excel():
    file_path = "/Users/datashan/Desktop/Test Automation/PyAPIAutomationFramework/tests/crud/ddt_testing_usingExcel/ddt_test_data.xlsx"
    credentials = read_credentials_from_file(file_path=file_path)
    print(credentials)
    for user_cred in credentials:
        username = user_cred['username']
        password = user_cred['password']
        response = create_auth_req(username=username, password=password)
        print(response)
