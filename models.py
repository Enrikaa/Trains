class Locomative:

    def __init__(self, locomative_own_mass, max_towable_mass):
        self.own_mass = locomative_own_mass
        self.max_towable_mass = max_towable_mass

    def serialize_locomatives(self) -> dict:
        locomatives_dictionary = {"locomative_own_mass_in_metric_tones": self.own_mass,
                                  "locomative_max_towable_mass": self.max_towable_mass}
        return locomatives_dictionary


class Wagon:

    def __init__(self, specific_mass, load_carried_mass, max_load_mass, unique_wagon_number):
        self.specific_mass = specific_mass
        self.load_carried_mass = load_carried_mass
        self.max_load_mass = max_load_mass
        self.unique_wagon_number = unique_wagon_number

    def serialize_wagons(self) -> dict:
        wagons_dictionary = {"wagon_specific_mass": self.specific_mass,
                             "wagon_load_carried_mass": self.load_carried_mass,
                             "wagon_max_load_mass": self.max_load_mass,
                             "wagon_unique_wagon_number": self.unique_wagon_number}
        return wagons_dictionary


class Train:
    wagons_limit = 4

    def __init__(self, locomative_own_mass, max_towable_mass, wagons, wagons_mass=None):
        self.locomative = Locomative(locomative_own_mass, max_towable_mass)
        self.wagons = [i for i in wagons]
        self.wagons_mass = wagons_mass

    def serialize_train(self) -> dict:
        locomative = self.locomative.serialize_locomatives()
        train_dict = {"train": {"locomative": locomative, "wagons": self.wagons},
                      "train_wagons_mass": self.wagons_mass}
        return train_dict
