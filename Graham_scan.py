from matplotlib import pyplot as plt
from math import atan2
from random import randint
import config
import loading_data


def scatter_plot(points, convex_hull=None):
    for set_of_points in points:
        xs, ys = zip(*set_of_points)
        plt.scatter(xs, ys)

    if convex_hull != None:
        for i in range(1, len(convex_hull)+1):
            if i == len(convex_hull):
                i = 0
            c0 = convex_hull[i-1]
            c1 = convex_hull[i]
            plt.plot((c0[0], c1[0]), (c0[1], c1[1]), "r")
    plt.show()


def polar_angle(p0, p1=None):
    if p1 == None:
        p1 = anchor
    y_span = p0[1] - p1[1]
    x_span = p0[0] - p1[0]
    return atan2(y_span, x_span)


def get_distance(p0, p1=None):
    if p1 == None:
        p1 = anchor
    y_span = p0[1] - p1[1]
    x_span = p0[0] - p1[0]
    return y_span**2 + x_span**2


def det(p1,p2,p3):
    return (p2[0]-p1[0])*(p3[1]-p1[1]) \
                  -(p2[1]-p1[1])*(p3[0]-p1[0])


def quicksort(a):
    if len(a) <= 1:
        return a
    smaller, equal, larger = [], [], []
    piv_ang = polar_angle(a[randint(0, len(a)-1)])
    for pt in a:
        pt_ang = polar_angle(pt)
        if pt_ang < piv_ang:
            smaller.append(pt)
        elif pt_ang == piv_ang:
            equal.append(pt)
        else:
            larger.append(pt)
    return quicksort(smaller) \
            +sorted(equal, key=get_distance) \
            +quicksort(larger)


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
        sorted_points = quicksort(sets)
        del sorted_points[sorted_points.index(anchor)]
        hull = [anchor, sorted_points[0]]
        for s in sorted_points[1:]:
            while det(hull[-2], hull[-1], s) <= 0:
                del hull[-1]
                #if len(hull)<2: break
            hull.append(s)
            if show_progress:
                scatter_plot(sets, hull)
        return hull


def main():
    map0 = config.MAPS["map_0"]
    map1 = config.MAPS["map_1"]
    points = loading_data.loading_map(map1)
    graham_scan(points, True)
    scatter_plot(points, graham_scan(points, True))


if __name__ == "__main__":
    main()