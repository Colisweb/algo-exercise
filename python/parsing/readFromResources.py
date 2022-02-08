from domain.Point import Point
from domain.Edge import Edge
from domain.PathProblem import PathProblem


def unwrapCycle(line: str) -> Point:
    _, x, y, *_ = line.split(" ")
    return Point(x, y)


def cycle(filename: str) -> "list[Point]":
    with open(f"resources/cycle/{filename}") as file:
        maze: "list[str]" = [line for line in file.read().splitlines() if line]
    return list(map(unwrapCycle, maze))


def neighbors(row: int, col: int) -> "iter[Point]":
    return map(lambda r, c: Point(r, c),
               [row, row, row + 1, row - 1],
               [col + 1, col - 1, col, col])


def findChar(maze: "list[str]", c: str) -> Point:
    row: int = next((index for index, val in enumerate(maze) if c in val), None)
    col: int = maze[row].find(c)
    return Point(row, col)


def path(filename: str) -> PathProblem:
    with open(f"resources/path/{filename}") as file:
        maze: "list[str]" = file.read().splitlines()

    edges: "list[Edge]" = [Edge(Point(rowIndex, colIndex), neighbor)
                           for rowIndex in range(len(maze))
                           for colIndex in range(len(maze[rowIndex]))
                           if maze[rowIndex][colIndex] != "#"
                           for neighbor in neighbors(rowIndex, colIndex)
                           if neighbor.x >= 0 and neighbor.x < len(maze)
                           and neighbor.y >= 0 and neighbor.y < len(maze[int(neighbor.x)])
                           and maze[int(neighbor.x)][int(neighbor.y)] != "#"]

    return PathProblem(edges, findChar(maze, "S"), findChar(maze, "E"))
