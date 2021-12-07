import json


def read_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

