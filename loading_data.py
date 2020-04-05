import json

with open('map_data_0.json') as map_data_0:
  data = json.load(map_data_0)

print(data)


map_name = data["map_name"]
map_units = data["units"]
#map_coordinates = data["object"][0]["coordinates"]
map_shapes = data["object"]

map_shapes_count = len(map_shapes)

counter = 0
points = []
shape_names = []
for shape in map_shapes:
    points.append(shape["coordinates"])
    shape_names.append(shape["name"])
    counter += 1


print(data.map_name)
