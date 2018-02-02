import unittest
from api.travel_collector import Google_API

class APITests(unittest.TestCase):
    
    def test_that_the_google_API_returns_status_OK(self):
        google_API = Google_API("Frejgatan+16", "driving", 1519822190)
        status = google_API.check_status_OK()
        self.assertTrue(status)

