import matplotlib.pyplot as plt
import loading_data
import config


def draw_points(points):
    """
    Tato funkce vykreslí body v grafu
    :param points: seznam bodů jednotlivých překážek importovaných z modulu loading_data.py
    :return: graf bodů
    """
    xs = []
    xy = []
    for set_of_points in points:
        x,y = zip(*set_of_points)
        print(x,y)
        plt.scatter(x, y)
        plt.plot(x, y)  #spojí jednotlivé body tvořící překážku
        #plt.show()      #vykreslí body jednotlivých překážek do grafu
        for index in range(len(x)):
            xs.append(x[index])
        for index in range(len(y)):
            xy.append(y[index])

    plt.scatter(xs, xy)
    return plt.show()       #vykreslí body všech překážek najednou do jednoho grafu


def main():
    map0 = config.MAPS["map_0"]
    map1 = config.MAPS["map_1"]
    points = loading_data.loading_map(map1)
    draw_points(points)


if __name__ == "__main__":
    main()


