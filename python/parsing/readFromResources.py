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


def findChar(maze: "list[str]", c: str) -> Point:
    row: int = next(index for index, val in enumerate(maze) if c in val, None)
    col: int = maze[row].find(c)
    return Point(row, col)


def path(filename: str) -> PathProblem:
    with open(f"path/{filename}") as file:
        maze = file.read().splitlines()

    edges = [Edge(Point(rowIndex, colIndex), neighbor)
            for rowIndex in range(maze)
            for colIndex in range(maze[rowIndex])
            if maze[rowIndex][colIndex] != "#"
            for neighbor in neighbors(rowIndex, colIndex)
            if neighbor.x < len(maze)
            for neighborRow in maze[neighbor.x]
            if neighbor.y < len(neighborRow)
            for neighborCell in neighborRow[neighbor.y]
            if neighborCell != "#"]

    return PathProblem(edges, findChar(maze, "S"), findChar(maze, "E"))
