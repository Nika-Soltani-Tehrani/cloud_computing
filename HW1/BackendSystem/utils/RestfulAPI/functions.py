import json


def json_loader(filepath):
    with open(filepath, 'r') as f:
        data = json.loads(f.read())
        return data