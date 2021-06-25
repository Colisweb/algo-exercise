from domain.Edge import Edge
from domain.Path import Path
from domain.Point import Point
from domain.PathProblem import PathProblem
from sys import getrecursionlimit
from itertools import groupby


def shortestPath(pathProblem: PathProblem) -> Path:
    return Path(straightener(pathProblem.graph, unlooper([pathProblem.start] + aStar(pathProblem.graph, pathProblem.start, pathProblem.end, [], []))))


def aStar(graph: "list[Edge]", current: Point, end: Point, explored: "list[Point]", notExplored: "list[Point]", deep: int = 0) -> "list[Point]":
    if deep == getrecursionlimit()-20:
        print("too much")
        return []
    if current == end:
        print(deep)
        return []

    explored.append(current)

    notExploredNeighbors = [edge.to
                            for edge in graph
                            if edge.from_ == current
                            and edge.to not in explored]

    if notExploredNeighbors:
        notExploredNeighbors = sorted(notExploredNeighbors, key=lambda x: Edge(x, end).distance())
        current = notExploredNeighbors[0]
        notExplored += notExploredNeighbors[1::-1]  # voir sans le reverse

    else:
        current = notExplored.pop()

    return [current] + aStar(graph, current, end, explored, notExplored, deep+1)


def unlooper(path: "list[Point]", pos: int = 1) -> "list[Point]":
    if pos == len(path):
        return []

    neighbors = [(id, point) for id, point in enumerate(path[pos:]) if point.isNeighbor(path[pos - 1])]

    # group list by point
    neighbors = [s for k, g in ((k, list(g)) for k, g in groupby(neighbors, key=lambda s: s[1])) if not k or len(g) == 1 for s in g]

    diff, next = neighbors[-1]

    return [next] + unlooper(path, pos + diff + 1)


def straightener(graph: "list[Edge]", path: "list[Point]", pos: int = 0):
    if pos + 4 == len(path):
        return path[-4:]

    current = path[pos]
    next = path[pos + 4]

    if current.x == next.x:
        bridge = Point(next.x, next.y - 1)
        if current.y == next.y - 2 and Edge(current, bridge) in graph:
            return [current, bridge] + straightener(graph, path, pos + 4)

        bridge = Point(next.x, next.y + 1)
        if current.y == next.y + 2 and Edge(current, bridge) in graph:
            return [current, bridge] + straightener(graph, path, pos + 4)

    if current.y == next.y:
        bridge = Point(next.x - 1, next.y)
        if current.x == next.x - 2 and Edge(current, bridge) in graph:
            return [current, bridge] + straightener(graph, path, pos + 4)

        bridge = Point(next.x + 1, next.y)
        if current.x == next.x + 2 and Edge(current, bridge) in graph:
            return [current, bridge] + straightener(graph, path, pos + 4)

    return [path[pos]] + straightener(graph, path, pos + 1)
