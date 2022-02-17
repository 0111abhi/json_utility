import json
import logging

class Json_Utility:
    @classmethod
    def flatten_json(cls, json_str):
        def flatten(json_obj):
            flattened_json = {}
            for key, val in json_obj.items():
                if type(val) != dict:
                    flattened_json[key] = val
                else:
                    flattened_val = flatten(val)
                    for f_key, f_val in flattened_val.items():
                        flattened_json[key + "." + f_key] = f_val
            return flattened_json
        
        try:
            json_obj = json.loads(json_str)
        except:
            logging.error(f"Could not parse Json. {json_str}")
            print("Please enter valid json")
            return
        
        flattened_json_obj = flatten(json_obj)
        return json.dumps(flattened_json_obj)
