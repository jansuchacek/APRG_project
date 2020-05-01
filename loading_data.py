import json
import config


def loading_map(map):
    """
    Tato funkce načte mapu
    :param map: zadaná vstupní data
    :return: výstupem funkce bude seznam souřadnic
    """
    with open(map["PATH"]) as map["NAME"]:
        data = json.load(map["NAME"])

    #print(data)

    map_name = data["map_name"]
    map_units = data["units"]
    #map_coordinates = data["object"][0]["coordinates"]
    map_objects = data["object"]
    map_objects_count = len(map_objects)

    points = []
    object_names = []
    for object in map_objects:
        object_names.append(object["name"])
        if len(object["coordinates"]) > 2:
            points.append(object["coordinates"])

    return points


def load_start_and_end(test_path):
    """
    Tato funkce načte startovní a cílovou pozici
    :param test_path: zadaná vstupní data
    :return: Výstupem této funkce bude startovní a cílová poizce
    """
    with open(test_path["PATH"]) as test_path["NAME"]:
        data = json.load(test_path["NAME"])

    #print(data)

    starts_and_ends = data["path"]

    starts = []
    ends = []
    for dct in starts_and_ends:
        starts.append(dct["start"])
        ends.append(dct["end"])

    return starts, ends


def main():
    """Hlavní funkce"""

    map0 = config.MAPS["map_0"]
    map1 = config.MAPS["map_1"]
    points = loading_map(map0)
    print("points:", points)

    test_path = config.TEST_PATH["test_path"]
    starts, ends = load_start_and_end(test_path)
    print("starts:", starts, ",", "ends:", ends)


if __name__ == "__main__":
    main()

