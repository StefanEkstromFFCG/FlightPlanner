import apicaller
import datetime
import storedata
import json


def departing_flights(api, fly_from=None, date_from=None, date_to=None):
    """handles requests towards skypicker api"""
    parameters = {
        "flyFrom" : fly_from,
        "dateFrom" : date_from,
        "dateTo" : date_to
    }

    if date_from:
        formated_date_from = datetime.datetime.strptime(date_from, "%d/%m/%Y").date()
        current_date = datetime.date.today()
        if formated_date_from < current_date:
            raise ValueError("Please enter current or future date")

    return api.get_request_to_API(parameters)["data"]


base_url = "https://api.skypicker.com/flights"
skypicker_api = apicaller.APIcaller(base_url)

fly_from = "ARN"
date_from = "07/02/2018"
date_to = "07/02/2018"
now = datetime.date.today()
flights_from_ARN = departing_flights(skypicker_api, fly_from=fly_from, date_from=date_from, date_to=date_to)
# flattened_data = storedata.flatten_all_objects(flights_from_ARN)
storedata.format_data_and_write_to_csv("flightdata.csv", flights_from_ARN)







