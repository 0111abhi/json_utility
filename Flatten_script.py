import sys
from Json_Utility import Json_Utility

print(Json_Utility.flatten_json(sys.stdin.read()))
