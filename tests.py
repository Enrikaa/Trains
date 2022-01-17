from unittest.mock import patch

from main import get_train
from models import Locomative, Wagon, Train
from utils.helpers import *
from utils.tests_utils import *


@patch("main.locomative_own_mass", return_value=1)
@patch("main.locomative_max_towable_mass", return_value=2)
@patch("main.wagon_load_carried_mass", return_value=1)
@patch("main.wagon_max_load_mass", return_value=12)
@patch("main.wagon_unique_wagon_number", return_value=2)
class TestTrain(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.locomative = Locomative(locomative_own_mass=10, max_towable_mass=8)

        self.wagon1 = Wagon(specific_mass=2, load_carried_mass=3, max_load_mass=2, unique_wagon_number=1)
        self.wagon2 = Wagon(specific_mass=2, load_carried_mass=3, max_load_mass=2, unique_wagon_number=1)
        self.wagon3 = Wagon(specific_mass=2, load_carried_mass=3, max_load_mass=2, unique_wagon_number=1)

        self.serialized_wagon_1 = self.wagon1.serialize_wagons()
        self.serialized_wagon_2 = self.wagon2.serialize_wagons()
        self.serialized_wagon_3 = self.wagon3.serialize_wagons()

        self.wagons_list = [self.serialized_wagon_3, self.serialized_wagon_2]
        self.wagons_list2 = [self.serialized_wagon_3, self.serialized_wagon_2, self.serialized_wagon_1]

        self.to_many_wagons = [self.serialized_wagon_3, self.serialized_wagon_2,
                               self.serialized_wagon_1, self.serialized_wagon_3,
                               self.serialized_wagon_2]

        self.train1 = Train(self.locomative.own_mass, self.locomative.max_towable_mass,
                            self.wagons_list, self.wagons_specific_mass_sum_1)
        self.train2 = Train(self.locomative.own_mass, self.locomative.max_towable_mass,
                            self.wagons_list, self.wagons_specific_mass_sum_2)

        self.trains_instances = [self.train1, self.train2]
        self.wagons_specific_mass_sum = 4
        self.two_trains_list = []

    def test_save_data_in_json(self, wagon_unique_wagon_number, wagon_max_load_mass, wagon_load_carried_mass,
                               locomative_max_towable_mass, locomative_own_mass):
        serialized_trains = []
        for train in self.trains_instances:
            serialized_train = train.serialize_train()
            serialized_trains.append(serialized_train)

        save_data_to_json_file(serialized_trains, self.main_json_filename)
        expected = read_json_files(self.main_json_filename)
        self.assertEqual(expected, self.json_test_data)
        self.assertEqual(2, len(serialized_trains))
        self.assertIs(type(serialized_trains), list)
        self.assertIs(type(serialized_trains[0]), dict)

    @patch("main.write_or_upload_file", return_value="upload")
    @patch("main.load_file_name", return_value="data_files/user_data_1.txt")
    @patch("utils.train_tasks.upload_file_to_json")
    def test_file_uploading_success(self, write_or_upload, get_load_file_name, upload_file_to_json,
                                    wagon_unique_wagon_number, wagon_max_load_mass, wagon_load_carried_mass,
                                    locomative_max_towable_mass, locomative_own_mass):
        get_user_data_output = get_train()
        loaded_files_in_json = read_json_files("data_files/user_data_1.json")
        self.assertTrue(upload_file_to_json.called)
        self.assertEqual(get_user_data_output, 'Your data_files now in user_data_1.json')
        self.assertEqual(loaded_files_in_json, self.expected_user_file_info)
        self.assertTrue(upload_file_to_json.called)

    @patch("main.write_or_upload_file", return_value="write")
    @patch("main.wagons_sum", return_value=1)
    @patch("main.wagon_specific_mass", return_value=100)
    @patch("main.another_train_question", return_value='no')
    def test_excessive_specific_mass_of_wagons(self, another_train, wagon_specific_mass, wagons_amount, write_or_upload,
                                               wagon_unique_wagon_number, wagon_max_load_mass, wagon_load_carried_mass,
                                               locomative_max_towable, locomative_own_mass):
        with self.assertRaises(TrainIsToHeavyException):
            get_train()

    @patch("main.write_or_upload_file", return_value="write")
    @patch("main.wagons_sum", return_value=100)
    @patch("main.wagon_specific_mass", return_value=1)
    @patch("main.another_train_question", return_value='no')
    def test_wrong_wagons_amount(self, another_train, wagon_specific_mass, wagons_amount, write_or_upload,
                                 wagon_unique_wagon_number, wagon_max_load_mass, wagon_load_carried_mass,
                                 locomative_max_towable, locomative_own_mass):
        with self.assertRaises(ToManyWagonsException):
            get_train()

    def test_full_train_serializing(self, wagon_unique_wagon_number, wagon_max_load_mass, wagon_load_carried_mass,
                                    locomative_max_towable_mass, locomative_own_mass):

        wagon1 = Wagon(specific_mass=1, load_carried_mass=3, max_load_mass=2, unique_wagon_number=1)
        wagon2 = Wagon(specific_mass=1, load_carried_mass=3, max_load_mass=2, unique_wagon_number=1)

        wagons_list = [wagon1, wagon2]

        wagons_specific_mass_sum = 0
        for i in wagons_list:
            wagons_specific_mass_sum += i.specific_mass

        train = Train(self.locomative.own_mass, self.locomative.max_towable_mass,
                      self.wagons_list,
                      wagons_specific_mass_sum)

        serialize_train = train.serialize_train()
        self.assertEqual(serialize_train, self.serialized_train_with_two_wagons)
        self.assertEqual(len(serialize_train), 2)
        self.assertIs(type(serialize_train), dict)
