import Graham_scan
from matplotlib import pyplot as plt
import config
import loading_data


def main():
    """
    Pomocí této funkce spouštíme celý program
    :return: Výstup modulu Graham_scan.py, který vytvoří konvexní obaly překážek a zobrazí je v grafu.
    """
    #Výběr mapy:
    map0 = config.MAPS["map_0"]
    map1 = config.MAPS["map_1"]
    points = loading_data.loading_map(map0)

    for sets in points:
        Graham_scan.zobrazeni_bodu(sets, Graham_scan.graham_scan(sets))
    return plt.show()


if __name__ == "__main__":
    main()


