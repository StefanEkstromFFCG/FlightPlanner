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
                }]
    }
    return data
        


# @pytest.mark.usefixtures(json_data)
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