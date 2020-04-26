import math

inf = float("inf")

def get_closest_point(relevant_objects, start):
    min_distance = inf
    closest_point = [inf, inf]
    for object in relevant_objects:  # vyberie najblizsi bod z prekazok ktore stoja v ceste
        for point in object:
            distance = get_distance(start, point)
            if distance < min_distance:
                min_distance = distance
                closest_point = point
            else:
                continue

    for object in relevant_objects:
        if closest_point in object:
            closest_object = object

    if closest_point == start:
        index = closest_object.index(closest_point)
        length = len(closest_object) - 1
        if closest_object.index(closest_point) == length:
            closest_point = closest_object[0]
        else:
            closest_point = closest_object[index + 1]

    return closest_point, closest_object

def get_distance(p1, p2):
    return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))