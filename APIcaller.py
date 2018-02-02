import time 
import requests

class APIcaller():
    def __init__(self, baseurl, parameters):
        self.base_url = baseurl
        self.parameters = parameters

    def get_request_to_API(self):
        """calls the API with a get request and returns the response"""
        current_delay = 0.1  # Set the initial retry delay to 100ms.
        max_delay = 3600  # Set the maximum retry delay to 1 hour.

        while True:
            try:
                # Get the API response.
                response = requests.get(self.base_url, params=self.parameters)
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

    def check_status(self):
        return requests.get(self.base_url, params=self.parameters).status_code