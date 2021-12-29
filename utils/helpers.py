import json
from typing import List, Dict


class ToManyWagonsException(Exception):
    pass


class TrainIsToHeavyException(Exception):
    pass


def save_data_to_json_file(data: List[Dict], filename: str) -> None:
    with open(filename, "w") as f:
        json.dump(data, f)
        f.write('\n')


def read_json_files(filename: str) -> str:
    try:
        with open(filename, "r") as json_file:
            json_data = json_file.read()
            obj = json.loads(json_data)
            return obj
    except json.decoder.JSONDecodeError:
        return "error_string_could_not_be_converted_to_JSON_file"
