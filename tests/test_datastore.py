import unittest
import app.storedata as storedata
import pytest
# import json

@pytest.fixture()
def json_data():
    data = {"json" : [{
            "pk": 22, 
            "model": "auth.permission", 
            "fields": {
                "codename": "add_message", 
                "name": "Can add message", 
                "content_type": 8
                }
        },
                {
            "pk": 25, 
            "model": "auth.permission", 
            "fields": {
                "codename": "add_message", 
                "name": "Can add message", 
                "content_type": 108
                }
        }],
        "target_json" : [{
                    "pk": 22, 
                    "model": "auth.permission", 
                    "fields__codename": "add_message", 
                    "fields__name": "Can add message", 
                    "fields__content_type": 8
                },
                {
                    "pk": 25, 
                    "model": "auth.permission", 
                    "fields__codename": "add_message", 
                    "fields__name": "Can add message", 
                    "fields__content_type": 108
                }],
        "flights_data" : [
        {
            "mapIdfrom": "stockholm",
            "duration": {
                "total": 9600,
                "return": 0,
                "departure": 9600
            },
            "flyTo": "BSL",
            "conversion": {
                "EUR": 100
            },
            "deep_link": "https://www.kiwi.com/deep?from=ARN&to=BSL&departure=08-02-2018&flightsId=3532731584995748_0&price=100&passengers=1&affilid=picky&lang=en&currency=EUR&booking_token=TjFsU9KOyjpEDqm5dNSrO1ZjuRMVMgZrERrSppD325T6P8+P9w468E+3gYirNKm0xjFEaQ8brFkJXYHcFnHHQMiKg0Dkoaiav5UhUit795hlDRZUq8aCyCTw4fdhJod+M1d5SBkLVg1lwCO7BMx27VCT3Q9Hrva2qEgOjLlVpj5UudFifyQk06/Q1fRgpWMLttxF/Rsa2KFpHeNOBIAe8qD3iItXqXEOyyBLNe/haERG1OWSTyvCq0tBWL307IfhOOb/DvWplr5UUU1EjUQqHdglL60JkUQRooqwhV2E4FEXciLiRSaK66yHDlJBfMlJNu2ZWjmfOOVknbosUTEv40cp+L4ujUbjyPIqW50Lv1gN6443+ogkBUD3/EKK5CuubyI5IkNZfE8G1bec/+0640LK4uy57LwHKHAxqijH8LPfeLrTPRdGJuLsDOP5lBqv4sVSPiyq/Ocp7Q3QbLvYhvPWK/n/+b2QNso+hFxyPNXe+9dN+ZS7BbSTIlR6TJY8eUGEPCf8kUnAlSewkkxOkFiD4lqpthuVth+YP1BjWNUU/BarAis3V+5Xxj39SwPLl+DQWA9EGNeylyvC6suUVs22YnVIKkt8Wf2vMH3JAoggmT/MWB0xXq7XyWwb1s/eBB3I7cmZTMpW/Hk5yWM+VD0WnjRSaLL6i1ZC01B829U=",
            "mapIdto": "freiburg",
            "nightsInDest": None,
            "airlines": [
                "U2"
            ],
            "id": "3532731584995748_0",
            "facilitated_booking_available": True,
            "pnr_count": 1,
            "fly_duration": "2h 40m",
            "countryTo": {
                "code": "CH",
                "name": "Switzerland"
            },
            "baglimit": {
                "hand_width": 45,
                "hand_length": 56,
                "hold_weight": 15,
                "hand_height": 25,
                "hand_weight": 15
            },
            "aTimeUTC": 1518123000,
            "p3": 1,
            "price": 100,
            "type_flights": [
                "lcc-U2"
            ],
            "bags_price": {
                "1": 21,
                "2": 46
            },
            "cityTo": "Basel",
            "transfers": [],
            "flyFrom": "ARN",
            "dTimeUTC": 1518113400,
            "p2": 1,
            "countryFrom": {
                "code": "SE",
                "name": "Sweden"
            },
            "p1": 1,
            "dTime": 1518117000,
            "found_on": [
                "deprecated"
            ],
            "booking_token": "TjFsU9KOyjpEDqm5dNSrO1ZjuRMVMgZrERrSppD325T6P8+P9w468E+3gYirNKm0xjFEaQ8brFkJXYHcFnHHQMiKg0Dkoaiav5UhUit795hlDRZUq8aCyCTw4fdhJod+M1d5SBkLVg1lwCO7BMx27VCT3Q9Hrva2qEgOjLlVpj5UudFifyQk06/Q1fRgpWMLttxF/Rsa2KFpHeNOBIAe8qD3iItXqXEOyyBLNe/haERG1OWSTyvCq0tBWL307IfhOOb/DvWplr5UUU1EjUQqHdglL60JkUQRooqwhV2E4FEXciLiRSaK66yHDlJBfMlJNu2ZWjmfOOVknbosUTEv40cp+L4ujUbjyPIqW50Lv1gN6443+ogkBUD3/EKK5CuubyI5IkNZfE8G1bec/+0640LK4uy57LwHKHAxqijH8LPfeLrTPRdGJuLsDOP5lBqv4sVSPiyq/Ocp7Q3QbLvYhvPWK/n/+b2QNso+hFxyPNXe+9dN+ZS7BbSTIlR6TJY8eUGEPCf8kUnAlSewkkxOkFiD4lqpthuVth+YP1BjWNUU/BarAis3V+5Xxj39SwPLl+DQWA9EGNeylyvC6suUVs22YnVIKkt8Wf2vMH3JAoggmT/MWB0xXq7XyWwb1s/eBB3I7cmZTMpW/Hk5yWM+VD0WnjRSaLL6i1ZC01B829U=",
            "routes": [
                [
                    "ARN",
                    "BSL"
                ]
            ],
            "cityFrom": "Stockholm",
            "aTime": 1518126600,
            "route": [
                {
                    "bags_recheck_required": False,
                    "mapIdfrom": "stockholm",
                    "flight_no": 1146,
                    "original_return": 0,
                    "lngFrom": 17.918611,
                    "flyTo": "BSL",
                    "guarantee": False,
                    "latTo": 47.601111,
                    "source": "deprecated",
                    "combination_id": "3532731584995748",
                    "id": "3532731584995748_0",
                    "latFrom": 59.651944,
                    "lngTo": 7.521667,
                    "dTimeUTC": 1518113400,
                    "aTimeUTC": 1518123000,
                    "return": 0,
                    "price": 1,
                    "cityTo": "Basel",
                    "vehicle_type": "aircraft",
                    "flyFrom": "ARN",
                    "mapIdto": "freiburg",
                    "dTime": 1518117000,
                    "found_on": "deprecated",
                    "airline": "U2",
                    "cityFrom": "Stockholm",
                    "aTime": 1518126600
                }
            ],
            "distance": 1502.8
        },
        {
            "mapIdfrom": "stockholm",
            "duration": {
                "total": 10200,
                "return": 0,
                "departure": 10200
            },
            "flyTo": "BRS",
            "conversion": {
                "EUR": 100
            },
            "deep_link": "https://www.kiwi.com/deep?from=ARN&to=BRS&departure=08-02-2018&flightsId=3527234017512062_0&price=100&passengers=1&affilid=picky&lang=en&currency=EUR&booking_token=TjFsU9KOyjpEDqm5dNSrO1ZjuRMVMgZrERrSppD325T6P8+P9w468E+3gYirNKm0xjFEaQ8brFkJXYHcFnHHQMiKg0Dkoaiav5UhUit795jwlbK911PNijl7eYOxulSkGzHpDCd7mD9Y/laljq7gTs6z4I1/tScNq7YubfKhvw5xy22gpuARChyVFi4o6pGAGkOrPNHvbiWFuQ8YEP2yjahIiMrB3f6AOUxXUnw9CmRW2h+gXbT/0NL9UwmzZu9+czI1en1oHWiSdEYicuOJH1fxPkwjh66dGEu3CevHFJnSsh86lT6mUOag1lVfKBQsEFT02zxluNvhIuoI2q988qo+oLx7k6xVYPZ+WcD9GPdNvLWy9jhjNqhe+RYQUX9F4jIg0LdgwqlBDjt1999qCoRMf/4W4nG45Eb8FmTmv6yNh92S34XvlBdzwO35RHRoL5vVygXBMZ6i+kav2MXohRAb1TDrkc/UXdbLqMDGjlWfrofFzJxAPYL+oWQgKKI+Exk1WNndH2SHYAtFs0KnTLFciX+aMHB1EH0oILdTpqp0hJRsd9Qd4YV8rZ0WzJR4wKtpAud6/WsIKGRLBbO6qRMhH02iHAJ1hVOKbW2vJZlY8nyxZ5atxs8G7eQsPEgunCUbCyV5GPVzt6vvpgDHZhG4AzDBdq+5i464um0OcAE=",
            "mapIdto": "bristol",
            "nightsInDest": None,
            "airlines": [
                "U2"
            ],
            "id": "3527234017512062_0",
            "facilitated_booking_available": True,
            "pnr_count": 1,
            "fly_duration": "2h 50m",
            "countryTo": {
                "code": "GB",
                "name": "United Kingdom"
            },
            "baglimit": {
                "hand_width": 45,
                "hand_length": 56,
                "hold_weight": 15,
                "hand_height": 25,
                "hand_weight": 15
            },
            "aTimeUTC": 1518116100,
            "p3": 1,
            "price": 100,
            "type_flights": [
                "lcc-U2"
            ],
            "bags_price": {
                "1": 21,
                "2": 46
            },
            "cityTo": "Bristol",
            "transfers": [],
            "flyFrom": "ARN",
            "dTimeUTC": 1518105900,
            "p2": 1,
            "countryFrom": {
                "code": "SE",
                "name": "Sweden"
            },
            "p1": 1,
            "dTime": 1518109500,
            "found_on": [
                "deprecated"
            ],
            "booking_token": "TjFsU9KOyjpEDqm5dNSrO1ZjuRMVMgZrERrSppD325T6P8+P9w468E+3gYirNKm0xjFEaQ8brFkJXYHcFnHHQMiKg0Dkoaiav5UhUit795jwlbK911PNijl7eYOxulSkGzHpDCd7mD9Y/laljq7gTs6z4I1/tScNq7YubfKhvw5xy22gpuARChyVFi4o6pGAGkOrPNHvbiWFuQ8YEP2yjahIiMrB3f6AOUxXUnw9CmRW2h+gXbT/0NL9UwmzZu9+czI1en1oHWiSdEYicuOJH1fxPkwjh66dGEu3CevHFJnSsh86lT6mUOag1lVfKBQsEFT02zxluNvhIuoI2q988qo+oLx7k6xVYPZ+WcD9GPdNvLWy9jhjNqhe+RYQUX9F4jIg0LdgwqlBDjt1999qCoRMf/4W4nG45Eb8FmTmv6yNh92S34XvlBdzwO35RHRoL5vVygXBMZ6i+kav2MXohRAb1TDrkc/UXdbLqMDGjlWfrofFzJxAPYL+oWQgKKI+Exk1WNndH2SHYAtFs0KnTLFciX+aMHB1EH0oILdTpqp0hJRsd9Qd4YV8rZ0WzJR4wKtpAud6/WsIKGRLBbO6qRMhH02iHAJ1hVOKbW2vJZlY8nyxZ5atxs8G7eQsPEgunCUbCyV5GPVzt6vvpgDHZhG4AzDBdq+5i464um0OcAE=",
            "routes": [
                [
                    "ARN",
                    "BRS"
                ]
            ],
            "cityFrom": "Stockholm",
            "aTime": 1518116100,
            "route": [
                {
                    "bags_recheck_required": False,
                    "mapIdfrom": "stockholm",
                    "flight_no": 6034,
                    "original_return": 0,
                    "lngFrom": 17.918611,
                    "flyTo": "BRS",
                    "guarantee": False,
                    "latTo": 51.3825,
                    "source": "deprecated",
                    "combination_id": "3527234017512062",
                    "id": "3527234017512062_0",
                    "latFrom": 59.651944,
                    "lngTo": -2.718889,
                    "dTimeUTC": 1518105900,
                    "aTimeUTC": 1518116100,
                    "return": 0,
                    "price": 1,
                    "cityTo": "Bristol",
                    "vehicle_type": "aircraft",
                    "flyFrom": "ARN",
                    "mapIdto": "bristol",
                    "dTime": 1518109500,
                    "found_on": "deprecated",
                    "airline": "U2",
                    "cityFrom": "Stockholm",
                    "aTime": 1518116100
                }
            ],
            "distance": 1582.73
        }]
    }
    return data
        



class StoreTests(unittest.TestCase):
    def test_that_flatten_json_converts_to_flat_format(self):
        json_file = {
            "pk": 22, 
            "model": "auth.permission", 
            "fields": {
                "codename": "add_message", 
                "name": "Can add message", 
                "content_type": 8
                }
        }
        target_json = {
                    "pk": 22, 
                    "model": "auth.permission", 
                    "fields__codename": "add_message", 
                    "fields__name": "Can add message", 
                    "fields__content_type": 8
                }

        flatted_json = storedata.flatten_json(json_file, "__")
        assert flatted_json == target_json

    def test_that_column_finder_find_relevant_columns(self):
        json = [{
                    "pk": 22, 
                    "model": "auth.permission", 
                    "fields__codename": "add_message", 
                    "fields__name": "Can add message", 
                    "fields__content_type": 8
                },
                {
                    "pk": 22, 
                    "model": "auth.permission", 
                    "fields__codename": "add_message", 
                    "fields__name": "Can add message", 
                    "fields__content_type": 8
                }]
        
        columns = storedata.column_finder(json)
        self.assertCountEqual(["pk", "model", "fields__codename", "fields__name", "fields__content_type"], columns)

def test_that_flatten_all_objects_flattens_all_objects(json_data):
    case = unittest.TestCase()
    flattened_data = storedata.flatten_all_objects(json_data["json"])
    case.assertCountEqual(flattened_data, json_data["target_json"])

def test_that_flight_example_flattens_data_to_one_level(json_data):
    # flattened_data = storedata.flatten_all_objects(json_data["flights_data"])
    # print(flattened_data)
    storedata.format_data_and_write_to_csv("test.csv", json_data["flights_data"])
    assert True