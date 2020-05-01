import matplotlib.pyplot as plt
import loading_data
import config


def draw_points(points):
    """
    Tato funkce vykreslí body v grafu
    :param points: seznam bodů jednotlivých překážek importovaných z modulu loading_data.py
    :return: graf bodů
    """
    for set_of_points in points:
        x, y = zip(*set_of_points)
        print("x:", x, "y:", y)
        plt.scatter(x, y)
        plt.plot(x, y)      #spojí jednotlivé body tvořící překážku
    return plt.show()       #vykreslí body všech překážek najednou do jednoho grafu


def main():
    """Toto je řídící funkce"""

    map0 = config.MAPS["map_0"]
    map1 = config.MAPS["map_1"]
    points = loading_data.loading_map(map1)
    draw_points(points)


if __name__ == "__main__":
    main()


