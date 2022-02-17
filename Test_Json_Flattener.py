import unittest
import json
from Json_Utility import Json_Utility

class Test_Json_Flattener(unittest.TestCase):
    user_nested_json = {
            "name": "John",
            "address": {
                "state": "washington",
                "area":
                {
                    "street": 121,
                    "city": "Bellevue",
                    "zip": 98008
                },
                "same_as_mailing": True
            }
        }

    user_flattened_json = {
        "name": "John",
        "address.state": "washington",
        "address.area.street": 121,
        "address.area.city": "Bellevue",
        "address.area.zip": 98008,
        "address.same_as_mailing": True
    }
    
    def test_nested_json_flattens(self):
        flattened_ouput = Json_Utility.flatten_json(json.dumps(self.user_nested_json))
        self.assertEqual(json.dumps(self.user_flattened_json), flattened_ouput)
    
    def test_flattened_json_remains_unchanged(self):
        flattened_ouput = Json_Utility.flatten_json(json.dumps(self.user_flattened_json))
        self.assertEqual(json.dumps(self.user_flattened_json), flattened_ouput)

if __name__ == '__main__':
    unittest.main()