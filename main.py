import Graham_scan
from matplotlib import pyplot as plt
import config
import loading_data
import data_display


def main():
    """
    Pomocí této funkce spouštíme celý program
    :return: Výstup modulu Graham_scan.py, který vytvoří konvexní obaly překážek a zobrazí je v grafu.
    """
    #Výběr mapy:
    map0 = config.MAPS["map_0"]
    map1 = config.MAPS["map_1"]
    points = loading_data.loading_map(map0)

    #Zobrazení mapy:
    data_display.draw_points(points)

    #Počáteční a koncové body:
    test_path = config.TEST_PATH["test_path"]
    starts, ends = loading_data.load_start_and_end(test_path)
    print("Pocatecni body:", starts)
    print("Koncove body:", ends)

    #Graham scan:
    i = 1
    for sets in points:
        print("Polygon cislo", i, ":", sets)
        Graham_scan.zobrazeni_bodu(sets, Graham_scan.graham_scan(sets))
        i += 1
    return plt.show()


if __name__ == "__main__":
    main()