# imports
import json

def output(outputs):
    json_object = json.dumps(outputs, indent = 4)
    print(json_object)