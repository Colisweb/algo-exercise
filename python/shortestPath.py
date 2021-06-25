from domain.Edge import Edge
from domain.Path import Path
from domain.Point import Point
from domain.PathProblem import PathProblem
from sys import getrecursionlimit


def shortestPath(pathProblem: PathProblem) -> Path:
    return Path(cleaning([pathProblem.start]+aStar(pathProblem.graph, pathProblem.start, pathProblem.end, [], [], 0)))


def aStar(graph: "list[Edge]", current: Point, end: Point, explored: "list[Point]", notExplored: "list[Point]", deep: int) -> "list[Point]":
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
        notExplored += notExploredNeighbors[1::-1]

    else:
        current = notExplored.pop()

    return [current] + aStar(graph, current, end, explored, notExplored, deep+1)


def cleaning(path: "list[Point]") -> "list[Point]":
    return path
