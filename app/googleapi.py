"""Takes origin, mode of transportation and arrival time in epoch and returns the travel time
based on the Google directions API"""
from app.apicaller import APIcaller

class Google_API:
    """Class to handle the Google directions API from origin to ARN"""
    def __init__(self, origin, mode, arrival_time_epoch):
        self.mode = mode
        self.wanted_arrival_time = arrival_time_epoch
        self.parameters = self.initialize_parameters(origin, mode, arrival_time_epoch)
        self.directions_base_url = "https://maps.googleapis.com/maps/api/directions/json"
        self.google_directions_API = APIcaller(self.directions_base_url)
        self.response_data = None 

    def initialize_parameters(self, origin, mode, arrival_time_epoch):
        """Initializing the parameters for the Google API call"""
        parameters = {
            "origin" : origin,
            "destination" : "Arlanda+Airport",
            "mode" : mode,
            "key" : "AIzaSyByaBx4BgSWNQJyQebF5NP95VEAMRSVTYs"
            }

        if mode == "driving":
            parameters["traffic_model"] = "pessimistic"
            parameters["departure_time"] = arrival_time_epoch #Google API doesn't accept arrival_time as parameter for driving to return estimated travel time in traffic
        
        else:
            parameters["arrival_time"] = arrival_time_epoch
        return parameters
    
    def initialize_API(self):
        """initializes the API and if driving, updates the departure parameter to get correct arrival time since it cannot take the arrival time"""
        self.collect_data()

        if self.mode == "driving":
            difference_wanted_and_actual_time_of_arrival = self.wanted_arrival_time - self.get_estimated_time_of_arrival()
            tries = 0
            maximum_number_tries = 5

            while (difference_wanted_and_actual_time_of_arrival != 0) and (tries < maximum_number_tries):
                self.parameters["departure_time"] += difference_wanted_and_actual_time_of_arrival
                self.collect_data()
                difference_wanted_and_actual_time_of_arrival = self.wanted_arrival_time - self.get_estimated_time_of_arrival()
                tries +=1


    def collect_data(self):
        self.response_data = self.google_directions_API.get_request_to_API(self.parameters)["routes"][0]["legs"][0]

    def get_estimated_travel_time_seconds(self):
        """returns the travel time"""
        if self.mode=="driving":
            duration_parameter = "duration_in_traffic"
        else:
            duration_parameter = "duration"
        return self.response_data[duration_parameter]["value"]

    def get_estimated_time_of_arrival(self):
        """returns the estimated time of arrival"""
        if self.mode == "driving":
            eta = self.parameters["departure_time"] + self.get_estimated_travel_time_seconds()
        
        else:
            eta = self.response_data["arrival_time"]["value"]
        
        return eta

    def check_status_OK(self):
        return self.google_directions_API.check_status(self.parameters) == 200
        

# triptoarn = google_API("Frejgatan+16", "driving", 1517585822)
# print(triptoarn.get_estimated_travel_time_seconds())

triptoarn = Google_API("Frejgatan+16", "transit", 1519822990)
triptoarn.initialize_API()
print(triptoarn.get_estimated_travel_time_seconds())
print(triptoarn.get_estimated_time_of_arrival())
