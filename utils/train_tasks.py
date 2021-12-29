import json
from typing import List, Dict

from models import Train


def upload_file_to_json(user_filename: str) -> None:
    locomatives_values = []
    wagons = []
    wagons_values = []

    with open(user_filename) as file:
        lines = [line for line in file]

        for i in lines:
            if 'locomative' in i:
                locomatives_values.append(i)

            if 'wagon' in i:
                wagons_values.append(i)

        # Separate wagons
        for _ in wagons_values:
            wagons.append(wagons_values[:4:])
            del wagons_values[:4:]

    train = Train(locomatives_values[0], locomatives_values[1], wagons)

    out_file = open("data_files/user_data_1.json", "w")
    json.dump(train.serialize_train(), out_file, indent=4, sort_keys=False)
    out_file.close()


def sort_function(data: List[Train]) -> List[Dict]:
    sorted_trains_list = []
    sorted_trains = sorted(data, key=lambda train: train.wagons_mass)
    for train in sorted_trains:
        x = train.serialize_train()
        sorted_trains_list.append(x)
    return sorted_trains_list


def write_or_upload_file(text: str) -> str:
    while True:
        data = input(text)
        if data in ['write', 'upload']:
            return data
        else:
            print("Your data_files is incorrect, please try again:")


def load_file_name(text: str) -> str:
    while True:
        data = input(text)
        if data.find('txt') != -1:
            return data
        else:
            print("Your data_files format is incorrect, please try again:")


def locomative_own_mass(number: str) -> int:
    while True:
        data = input(number)
        if data.isnumeric():
            return int(data)
        else:
            print("Your data_files is incorrect, please try again:")


def locomative_max_towable_mass(number: str) -> int:
    while True:
        data = input(number)
        if data.isnumeric():
            return int(data)
        else:
            print("Your data_files is incorrect, please try again:")


def wagon_specific_mass(number: str) -> int:
    while True:
        data = input(number)
        if data.isnumeric():
            return int(data)
        else:
            print("Your data_files is incorrect, please try again:")


def wagon_load_carried_mass(number: str) -> int:
    while True:
        data = input(number)
        if data.isnumeric():
            return int(data)
        else:
            print("Your data_files is incorrect, please try again:")


def wagon_max_load_mass(number: str) -> int:
    while True:
        data = input(number)
        if data.isnumeric():
            return int(data)
        else:
            print("Your data_files is incorrect, please try again:")


def wagon_unique_wagon_number(number: str) -> int:
    while True:
        data = input(number)
        if data.isnumeric():
            return int(data)
        else:
            print("Your data_files is incorrect, please try again:")


def wagons_sum(number: str) -> int:
    while True:
        data = input(number)
        if data.isnumeric():
            return int(data)
        else:
            print("Your data_files is incorrect, please try again:")


def another_train_question(text: str) -> str:
    while True:
        data = str(input(text))
        if data in ['yes', 'no']:
            return data
        else:
            print("Your data_files is incorrect, please try again:")
