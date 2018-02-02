"""Takes origin, mode of transportation and departure time in epoch and returns the travel time
based on the Google directions API"""
import time
import requests

class TripToARN:
    """Class to handle the Google directions API from origin to ARN"""
    def __init__(self, origin, mode, departure_time_epoch):
        self.mode = mode
        self.parameters = self.set_parameters(origin, mode, departure_time_epoch)
        self.directions_base_url = "https://maps.googleapis.com/maps/api/directions/json"
        self.trip_data = self.collect_trip_information()

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

    def collect_trip_information(self):
        """returns the travel time from google directions API for selected mode of transportation"""
        current_delay = 0.1  # Set the initial retry delay to 100ms.
        max_delay = 3600  # Set the maximum retry delay to 1 hour.

        while True:
            try:
                # Get the API response.
                response = requests.get(self.directions_base_url, params=self.parameters)
            except IOError:
                pass  # Fall through to the retry loop.
            else:
                # If we didn't get an IOError then parse the result.
                result = response.json()
                if result['status'] == 'OK':
                    return result
                elif result['status'] != 'UNKNOWN_ERROR':
                    # Many API errors cannot be fixed by a retry, e.g. INVALID_REQUEST or
                    # ZERO_RESULTS. There is no point retrying these requests.
                    raise Exception(result['error_message'])

            if current_delay > max_delay:
                raise Exception('Too many retry attempts.')
            print('Waiting', current_delay, 'seconds before retrying.')
            time.sleep(current_delay)
            current_delay *= 2  # Increase the delay each time we retry.

    def get_estimated_travel_time_seconds(self):
        """returns the travel time"""
        if self.mode=="driving":
            duration_parameter = "duration_in_traffic"
        else:
            duration_parameter = "duration"
        return self.trip_data["routes"][0]["legs"][0][duration_parameter]["value"]

triptoarn = TripToARN("Frejgatan+16", "driving", 1517585822)
print(triptoarn.get_estimated_travel_time_seconds())

# triptoarn = TripToARN("Frejgatan+16", "driving", 1519822862)
# print(triptoarn.get_estimated_travel_time_seconds())
