from domain.Point import Point
from domain.Edge import Edge
from domain.PathProblem import PathProblem


def unwrapCycle(line: str) -> Point:
    _, x, y = line.split(" ")
    return Point(x, y)


def cycle(filename: str) -> "list[Point]":
    with open(f"cycle/{filename}") as file:
        maze = file.read().splitlines()
    return list(map(unwrapCycle, maze))


def neighbors(row: int, col: int) -> "list[Point]":  # , lastRow: int, lastCol: int
    return map((lambda r, c: Point(r, c)), [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)])


def unwrapPath(maze: "list[str]", x: int, y: int) -> Edge:
    return Edge(Point(0, 0), Point(0, 0))  # how?


def findChar(maze: "list[str]", c: str) -> Point:
    return Point(0, 0)  # how?


def path(filename: str) -> PathProblem:
    with open(f"path/{filename}") as file:
        maze = file.read().splitlines()

    # how?
    pointList = [_ for _ in maze for _ in maze]
    pointList = [unwrapPath(maze, x, y) for x in range(len(maze[0])) for y in range(len(maze))]

    return PathProblem(pointList, findChar(maze, "S"), findChar(maze, "E"))
