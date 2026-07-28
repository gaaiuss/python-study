"""
This module is meant to read a class data (attributes) from a json file.
"""

import json

from save_class_in_json_1 import save_data_local

with open(save_data_local) as file:
    hunter_data = json.load(file)

print(hunter_data)
