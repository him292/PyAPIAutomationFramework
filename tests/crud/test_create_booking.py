import allure
import pytest

class TestCreateBooking(object):
    @pytest.mark.pisitive
    @allure.title("Verify that create booking status and booking ID shouldnt be null")
    @allure.description("Test case to verify that create booking status and booking ID shouldnt be null")
    def test_create_booking_positive(self):
        pass