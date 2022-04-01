import json

def get_values_from_key(data, key_to_search):
    ans = []
    for key, value in data.items():
        if key == key_to_search:
            ans.append(value)
    return ans

def get_keys_from_values(data, value_to_search):
    ans = []
    for key, value in data.items():
        if value_to_search in value:
            ans.append(key)
        return ans

def load_json_data(file_path):
    with open(file_path, "r+") as database:
        return json.load(database)

def upload_json_data(file_path, data):
    with open(file_path, "r+") as database:
        database.write(json.dumps(data))
        return True
