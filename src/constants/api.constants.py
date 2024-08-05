# APIConstants - class which contains all the endpoints
# keeps the URLs

class APIConstants(object):

    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    def url_create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def url_update_booking(self, booking_id):
        return f"https://restful-booker.herokuapp.com/booking{booking_id}"

    def url_delete_booking(self, booking_id):
        return "https://restful-booker.herokuapp.com/booking/1"