import unittest


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.user_upload_filename = "data_files/user_data_1.txt"
        self.user_uploaded_filename = "data_files/user_data_1.json"
        self.main_json_filename = "data_files/data_files.json"

        self.wagons_specific_mass_sum_1 = 12
        self.wagons_specific_mass_sum_2 = 9

        self.json_test_data = \
            [{'train': {'locomative': {'locomative_max_towable_mass': 8, 'locomative_own_mass_in_metric_tones': 10},
                        'wagons': [{'wagon_load_carried_mass': 3, 'wagon_max_load_mass': 2, 'wagon_specific_mass': 2,
                                    'wagon_unique_wagon_number': 1},
                                   {'wagon_load_carried_mass': 3, 'wagon_max_load_mass': 2, 'wagon_specific_mass': 2,
                                    'wagon_unique_wagon_number': 1}]}, 'train_wagons_mass': 12}, {
                 'train': {'locomative': {'locomative_max_towable_mass': 8, 'locomative_own_mass_in_metric_tones': 10},
                           'wagons': [{'wagon_load_carried_mass': 3, 'wagon_max_load_mass': 2, 'wagon_specific_mass': 2,
                                       'wagon_unique_wagon_number': 1},
                                      {'wagon_load_carried_mass': 3, 'wagon_max_load_mass': 2, 'wagon_specific_mass': 2,
                                       'wagon_unique_wagon_number': 1}]}, 'train_wagons_mass': 9}]

        self.expected_user_file_info = {'train': {'locomative': {'locomative_max_towable_mass': 'locomative max '
                                                                                                'towable mass - 3\n',
                                                                 'locomative_own_mass_in_metric_tones': 'locomative '
                                                                                                        'own mass - '
                                                                                                        '2\n'},
                                                  'wagons': [['wagon specific mass - 1\n',
                                                              'wagon load carried mass - 3\n',
                                                              'wagon max load mass - 6\n',
                                                              'wagon unique number - 5\n'],
                                                             ['wagon specific mass - 1\n',
                                                              'wagon load carried mass - 3\n',
                                                              'wagon max load mass - 6\n',
                                                              'wagon unique number - 5\n']]},
                                        'train_wagons_mass': None}

        self.serialized_train_with_two_wagons = {
            'train': {'locomative': {'locomative_own_mass_in_metric_tones': 10, 'locomative_max_towable_mass': 8},
                      'wagons': [{'wagon_specific_mass': 2, 'wagon_load_carried_mass': 3, 'wagon_max_load_mass': 2,
                                  'wagon_unique_wagon_number': 1},
                                 {'wagon_specific_mass': 2, 'wagon_load_carried_mass': 3, 'wagon_max_load_mass': 2,
                                  'wagon_unique_wagon_number': 1}]}, 'train_wagons_mass': 2}
