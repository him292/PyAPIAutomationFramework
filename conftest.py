
# conftest file is used to keep the common code which needs to be run everytime we execute this framework. In our case, when
# creating a new booking, we'd be needing to create a new token as well as booking IDs in most cases, therefore, we added that
# code here so that python can run it before executing the test cases.
# scope=session so that these methods should be available to the entire project


from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils

import allure
import pytest
import openpyxl


@pytest.fixture(scope="session")
def create_token():
    response = post_request(
        url=APIConstants().url_create_token(),
        headers=Utils().common_headers_json(),
        auth=None,
        payload=payload_create_booking(),
        in_json=False
    )
    verify_http_status_code(response_data=response, expect_data=200)
    verify_json_key_for_not_null_token(response.json()["token"])
    return response.json()["token"]


@pytest.fixture(scope="session")
def get_booking_id():
    response = post_request(url=APIConstants().url_create_booking(),
                            auth=None,
                            headers=Utils().common_headers_json(),
                            payload=payload_create_booking(),
                            in_json=False)

    booking_id = response.json()["bookingid"]

    verify_http_status_code(response_data=response, expect_data=200)
    verify_json_key_for_not_null(booking_id)
    return booking_id