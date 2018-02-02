"""Takes origin, mode of transportation and departure time in epoch and returns the travel time
based on the Google directions API"""
from APIcaller import APIcaller

class Google_API:
    """Class to handle the Google directions API from origin to ARN"""
    def __init__(self, origin, mode, departure_time_epoch):
        self.mode = mode
        self.parameters = self.set_parameters(origin, mode, departure_time_epoch)
        self.directions_base_url = "https://maps.googleapis.com/maps/api/directions/json"
        self.google_directions_API = APIcaller(self.directions_base_url, self.parameters)
        self.response_data = None

    def set_parameters(self, origin, mode, departure_time_epoch):
        """Setting the parameters for the Google API call"""
        parameters = {
            "origin" : origin,
            "destination" : "Arlanda+Airport",
            "mode" : mode,
            "departure_time" : departure_time_epoch,
            "key" : "AIzaSyByaBx4BgSWNQJyQebF5NP95VEAMRSVTYs"
            }

        if mode == "driving":
            parameters["traffic_model"] = "pessimistic"
        return parameters

    def collect_data(self):
        self.response_data = self.google_directions_API.get_request_to_API()

    def get_estimated_travel_time_seconds(self):
        """returns the travel time"""
        if self.mode=="driving":
            duration_parameter = "duration_in_traffic"
        else:
            duration_parameter = "duration"
        return self.response_data["routes"][0]["legs"][0][duration_parameter]["value"]

    def check_status_OK(self):
        return self.google_directions_API.check_status() == 200

# triptoarn = google_API("Frejgatan+16", "driving", 1517585822)
# print(triptoarn.get_estimated_travel_time_seconds())

triptoarn = Google_API("Frejgatan+16", "driving", 1519822190)
triptoarn.collect_data()
print(triptoarn.get_estimated_travel_time_seconds())
