import json
from core.config import JSON_FILES_PATH

def read_json_7(file_name = 'comb7_list.json') -> dict:
    with open(f'{JSON_FILES_PATH}/{file_name}', 'r') as file:
        data = json.load(file)
        return data
    