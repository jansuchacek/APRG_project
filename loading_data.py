import json


def loading_map():
    """
    Tato funkce načte mapu
    :return: výstupem funkce bude seznam souřadnic
    """
    with open('map_data_0.json') as map_data_0:
        data = json.load(map_data_0)

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


def load_start_and_end():
    """
    Tato funkce načte startovní a cílovou pozici
    :return: Výstupem této funkce bude startovní a cílová poizce
    """
    with open('test_path.json') as test_path:
        data = json.load(test_path)

    #print(data)

    starts_and_ends = data["path"]

    starts = []
    ends = []
    for dct in starts_and_ends:
        starts.append(dct["start"])
        ends.append(dct["end"])

    return starts, ends


def main():
    points = loading_map()
    print("points:", points)
    starts, ends = load_start_and_end()
    print("starts", starts, "ends", ends)


if __name__ == "__main__":
    main()
