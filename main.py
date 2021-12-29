from typing import List, Dict

from models import Wagon, Locomative, Train
from utils.helpers import save_data_to_json_file, TrainIsToHeavyException, \
    ToManyWagonsException
from utils.train_tasks import write_or_upload_file, load_file_name, locomative_own_mass, locomative_max_towable_mass, \
    wagons_sum, \
    wagon_specific_mass, wagon_load_carried_mass, wagon_max_load_mass, wagon_unique_wagon_number, \
    another_train_question, sort_function, upload_file_to_json

write_load = "Write or upload data_files?"
file_name = "Write your file name (should be in txt format)?"
l_mass = "Locomative mass (kg)"
l_towable_mass = "Locomative maximum towable mass (kg)"
w_carrier_mass = "Load carrier mass (kg)"
wagons_amount = "How many wagons do you need?"
w_specific_mass = "Wagon specific mass (kg)"
w_load_mass = "Maximum load mass (kg)"
w_number = "Wagon number"
another_train = "Do you want to create another train?"

trains_list: List[Train] = []
wagons_list: List[Dict[str, int]] = []


def get_train():
    """Get user input data_files and put it in json file.

       Keyword arguments:
       trains_list -- list of Train objects which will be uploaded in json
       wagons_list -- list of Wagon objects (the part of train_list)
       """

    wagons_specific_mass_sum: int = 0
    if write_or_upload_file(write_load) == 'upload':
        upload_file_to_json(load_file_name(file_name))
        return "Your data_files now in user_data_1.json"
    else:
        locomative = Locomative(locomative_own_mass(l_mass),
                                locomative_max_towable_mass(l_towable_mass))

        wagon_amount = wagons_sum(wagons_amount)
        for _ in range(wagon_amount):
            if wagon_amount < Train.wagons_limit:
                wagons = Wagon(wagon_specific_mass(w_specific_mass),
                               wagon_load_carried_mass(w_carrier_mass),
                               wagon_max_load_mass(w_load_mass),
                               wagon_unique_wagon_number(w_number))
                wagons_specific_mass_sum += wagons.specific_mass
                if wagons_specific_mass_sum > locomative.max_towable_mass:
                    raise TrainIsToHeavyException()
                wagons_list.append(wagons.serialize_wagons())
            else:
                raise ToManyWagonsException()

        train = Train(locomative.own_mass, locomative.max_towable_mass,
                      wagons_list,
                      wagons_specific_mass_sum)
        wagons_list.clear()
        trains_list.append(train)

    if another_train_question(another_train) == "yes":
        return get_train()
    else:
        save_data_to_json_file(sort_function(trains_list), "data_files/data.json")
        return "Have a nice day! We uploaded your trains information in data_files.json file"

get_train()