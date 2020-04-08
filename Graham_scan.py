from matplotlib import pyplot as plt
from math import atan2
from random import randint
import config
import loading_data


def display_points(points, convex_hull=None):
    for set_of_points in points:
        xs, ys = zip(*set_of_points)
        plt.scatter(xs, ys)

    if convex_hull != None:
        for i in range(1, len(convex_hull)+1):
            if i == len(convex_hull):
                i = 0
            h0 = convex_hull[i-1]
            h1 = convex_hull[i]
            plt.plot((h0[0], h1[0]), (h0[1], h1[1]), "r")
    plt.show()


def polar_angle(p0, p1=None):
    if p1 == None:
        p1 = anchor
    y_line = p0[1] - p1[1]
    x_line = p0[0] - p1[0]
    return atan2(y_line, x_line)


def get_distance(p0, p1=None):
    if p1 == None:
        p1 = anchor
    y_line = p0[1] - p1[1]
    x_line = p0[0] - p1[0]
    return atan2(y_line, x_line)


def determinant(p1,p2,p3):
    return (p2[0]-p1[0])*(p3[1]-p1[1]) \
                  -(p2[1]-p1[1])*(p3[0]-p1[0])


def angle_sort(a):
    if len(a) <= 1:
        return a
    smaller, equal, bigger = [], [], []
    piv_ang = polar_angle(a[randint(0, len(a)-1)])
    for pt in a:
        pt_ang = polar_angle(pt)
        if pt_ang < piv_ang:
            smaller.append(pt)
        elif pt_ang == piv_ang:
            equal.append(pt)
        else:
            bigger.append(pt)
    return angle_sort(smaller) \
            +sorted(equal, key=get_distance) \
            +angle_sort(bigger)


def graham_scan(points, show_progress=False):
    global anchor

    min_idx = None
    for sets in points:
        for i, (x, y) in enumerate(sets):
            if (min_idx == None) or (y < sets[min_idx][1]):
                min_idx = i
            if (y == sets[min_idx][1]) and (x < sets[min_idx][0]):
                min_idx = i
        anchor = sets[min_idx]
        sorted_points = angle_sort(sets)
        del sorted_points[sorted_points.index(anchor)]
        hull = [anchor, sorted_points[0]]
        for s in sorted_points[1:]:
            while determinant(hull[-2], hull[-1], s) <= 0:
                del hull[-1]
                #if len(hull)<2: break
            hull.append(s)
            if show_progress:
                display_points(sets, hull)
        return hull


def main():
    map0 = config.MAPS["map_0"]
    map1 = config.MAPS["map_1"]
    points = loading_data.loading_map(map1)
    graham_scan(points, True)
    display_points(points, graham_scan(points, True))


if __name__ == "__main__":
    main()