import json

def load_registry(file_path="sample_data/registry.json"):
    with open(file_path, "r") as file_obj:
        registry_data = json.load(file_obj)
    return registry_data

def lookup_plate(plate_number, registry_data):
    return registry_data.get(plate_number)