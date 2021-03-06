from matplotlib import pyplot as plt
from math import atan2
from random import randint
import config
import loading_data


def graham_scan(points):
    """
    Funkcia vytvorí konvexný obal ku každému polygonu mapy.
    :param points: body daného polygonu
    :return: vráti konvexnú obálku
    """
    global anchor   # premenná "anchor" nastavená ako globálna - najnižší bod

    min_index = None
    for i, (x, y) in enumerate(points):
        if (min_index == None) or (y < points[min_index][1]):
            min_index = i
        if (y == points[min_index][1]) and (x < points[min_index][0]):
            min_index = i
    anchor = points[min_index]
    sorted_points = razeni_podle_uhlu(points)
    del sorted_points[sorted_points.index(anchor)]
    hull = [anchor, sorted_points[0]]
    for point in sorted_points[1:]:
        while determinant(hull[-2], hull[-1], point) <= 0:
            del hull[-1]
        hull.append(point)
    return hull


def razeni_podle_uhlu(points):
    """
    Funkcia roztriedi dané body polygonu podľa narastajúceho uhlu medzi bodom "anchor".
    Body s rovnakými uhlami budú roztriedené podľa ich vzdialenosti k bodu "anchor".
    """
    if len(points) <= 1:
        return points
    smaller = []
    equal = []
    bigger = []
    random_angle = polarni_uhel(points[randint(0, len(points) - 1)])
    for pt in points:
        pt_angle = polarni_uhel(pt)
        if pt_angle < random_angle:
            smaller.append(pt)
        elif pt_angle == random_angle:
            equal.append(pt)
        else:
            bigger.append(pt)
    return razeni_podle_uhlu(smaller) \
           + sorted(equal, key=vzdalenost_bodu) \
           + razeni_podle_uhlu(bigger)


def polarni_uhel(p0, p1=None):
    """
    Funkcia vráti uhol medzi najnižším bodom P0 a ďalším iným bodom P1.
    Ak neexistuje bod P1, tak bude nahradený globálnou premennou "anchor".
    :param p0: najnižší bod polygonu
    :param p1: iný bod
    :return: vráti veľkosť uhlu - arctan
    """
    if p1 == None:
        p1 = anchor
    y_line = p0[1] - p1[1]  # odvesna y
    x_line = p0[0] - p1[0]  # odvesna x
    return atan2(y_line, x_line)


def vzdalenost_bodu(p0, p1=None):
    """
    Funkcia vráti súčet druhých mocnín odvesien ako vzdialenosť medzi bodom P0 a iným bodom P1.
    :param p0: najnižší bod polygonu
    :param p1: iný bod
    :return: vráti vzdialenosť
    """
    if p1 == None:
        p1 = anchor
    y_line = p0[1] - p1[1]
    x_line = p0[0] - p1[0]
    return y_line**2 + x_line**2


def determinant(p1, p2, p3):
    """
    Vráti determinant matice 3x3 troch po sebe nasledujúcich bodov polygonu:
        [p1(x) p1(y) 1]
	    [p2(x) p2(y) 1]
	    [p3(x) p3(y) 1]
	Ak determinant:
	    >0, tak priebeh hľadania konvexného obalu bude proti chodu hodinových ručičiek
	    <0, tak v smere hodinových ručičiek
	    =0, tak kolineárny smer
    """
    return (p2[0]-p1[0])*(p3[1]-p1[1]) \
           -(p2[1]-p1[1])*(p3[0]-p1[0])


def zobrazeni_bodu(points, convex_hull=None):
    """
    Funkcia zobrazí načítané dáta z mapy.
    :param points: jednotlivé polygony v mape
    :param convex_hull: ak != None, zobrazí konvexný obal k danému polygonu
    :return: zobrazí výsledok
    """

    x, y = zip(*points)
    plt.scatter(x, y)

    if convex_hull != None:
        for i in range(1, len(convex_hull)+1):
            if i == len(convex_hull):
                i = 0
            h0 = convex_hull[i-1]
            h1 = convex_hull[i]
            plt.plot((h0[0], h1[0]), (h0[1], h1[1]), "r")


def main():
    """Hlavná funkcia"""
    map0 = config.MAPS["map_0"]
    map1 = config.MAPS["map_1"]
    points = loading_data.loading_map(map1)

    for sets in points:
        print(sets)
        zobrazeni_bodu(sets, graham_scan(sets))
    plt.show()


if __name__ == "__main__":
    main()