import time 
import requests

class APIcaller():
    def __init__(self, baseurl):
        self.base_url = baseurl

    def get_request_to_API(self, parameters):
        """calls the API with a get request and returns the response"""
        current_delay = 0.1  # Set the initial retry delay to 100ms.
        max_delay = 3600  # Set the maximum retry delay to 1 hour.

        while True:
            try:
                # Get the API response.
                response = requests.get(self.base_url, params=parameters)
            except IOError:
                pass  # Fall through to the retry loop.
            else:
                # If we didn't get an IOError then parse the result.
                result = response.json()
                if response.status_code == 200:
                    return response.json()
                elif self.base_url.startswith("https://maps.googleapis.com/") and result['status'] != 'UNKNOWN_ERROR':
                    # Many API errors cannot be fixed by a retry, e.g. INVALID_REQUEST or
                    # ZERO_RESULTS. There is no point retrying these requests.
                    raise Exception(result['status'])
                

            if current_delay > max_delay:
                raise Exception('Too many retry attempts.')
            print('Waiting', current_delay, 'seconds before retrying.')
            time.sleep(current_delay)
            current_delay *= 2  # Increase the delay each time we retry.

    def check_status(self, parameters):
        return requests.get(self.base_url, params=parameters).status_code