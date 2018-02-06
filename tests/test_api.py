import unittest
from app.googleapi import Google_API
import time

class APITests(unittest.TestCase):
    
    def test_that_the_google_API_returns_status_OK(self):
        google_API = Google_API("Frejgatan+16", "driving", 1549179028)
        google_API.initialize_API()
        status = google_API.check_status_OK()
        self.assertTrue(status)

    def test_wanted_arrival_time_is_same_as_estimated_arrival_time_for_driving(self):
        wanted_time_of_arrival = 1549179028
        google_API = Google_API("Frejgatan+16", "driving", wanted_time_of_arrival)
        google_API.initialize_API()
        eta = google_API.get_estimated_time_of_arrival()
        self.assertEquals(wanted_time_of_arrival, eta)

    def test_wanted_arrival_time_is_same_or_less_than_estimated_arrival_time_for_transit(self):
        wanted_time_of_arrival = int(time.time()) + 520619 
        google_API = Google_API("Frejgatan+16+Stockholm", "transit", wanted_time_of_arrival)
        google_API.initialize_API()
        eta = google_API.get_estimated_time_of_arrival()
        self.assertLessEqual(eta, wanted_time_of_arrival)

