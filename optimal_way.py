import heapq
from typing import Union, List, Tuple

import networkx as nx
from sympy import Line, Polygon

Num = Union[int, float]

# A coordinate is a tuple of two numbers (int|float)
Coordinate = Tuple[Num, Num]

# Obstacle is a list of Coordinates
Obstacle = List[Coordinate]


class SimpleGraph:
    def __init__(self):
        self.edges = {}

    def neighbors(self, id):
        return self.edges[id]


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


class Pathfinder:
    def __init__(self, obstacles: List[Obstacle]):
        self.graph = self.build_graph(obstacles)

    def build_graph(self, obstacles: List[Obstacle]):
        graph = nx.Graph()

        polygons = []
        visited_lines = []

        for obst_coords in obstacles:
            poly = Polygon(*obst_coords)
            polygons.append(poly)

            coors_len = len(obst_coords)
            i = 0
            while i < coors_len:
                c1 = obst_coords[i]
                try:
                    c2 = obst_coords[i + 1]
                except IndexError:
                    c2 = obst_coords[-1]

                if c1 != c2:
                    visited_lines.append(Line(c1, c2))
                    graph.add_edge(c1, c2)

                i += 1

        coordinates = []

        # brute force the rest
        for obst_coords in obstacles:
            coordinates.extend(obst_coords)

        for coord1 in coordinates:
            for coord2 in coordinates:
                if coord1 == coord2:
                    continue

                l = Line(coord1, coord2)
                if l in visited_lines:
                    continue

                for poly in polygons:
                    intersect = l.intersection(poly)
                    if len(intersect) > 1:
                        graph.add_edge()


    @staticmethod
    def heuristic(a, b):
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)

    def _a_star_search(self, start, goal):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break

            for next in self.graph.neighbors(current):
                new_cost = cost_so_far[current] + self.graph.cost(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.heuristic(goal, next)
                    frontier.put(next, priority)
                    came_from[next] = current