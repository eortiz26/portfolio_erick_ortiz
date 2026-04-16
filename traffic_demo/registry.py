import json

def load_registry(path="sample_data/registry.json"):
    with open(path, "r") as file:
        return json.load(file)

def lookup_plate(plate_number, registry_data):
    return registry_data.get(plate_number)