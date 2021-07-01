from domain.Point import Point
from domain.Path import Path
from domain.Edge import Edge
from domain.PathProblem import PathProblem
from parsing.readFromResources import path
from shortestPath import shortestPath
import random
from functools import lru_cache


@lru_cache()
def gridNorthEast(width: int, height: int) -> "list[Edge]":
    return [elem for elemList in [[Edge(Point(x, y), Point(x + 1, y)),
                                   Edge(Point(x, y), Point(x, y + 1)),
                                   Edge(Point(x, y), Point(x + 1, y + 1))]
                                  for x in range(width)
                                  for y in range(height)]
            for elem in elemList]


def gridFull(width: int, height: int) -> "list[Edge]":
    return [elem for elemList in [[Edge(Point(x, y), Point(x + 1, y)),
                                   Edge(Point(x, y), Point(x, y + 1)),
                                   Edge(Point(x, y), Point(x, y - 1)),
                                   Edge(Point(x, y), Point(x - 1, y))]
                                  for x in range(width)
                                  for y in range(height)]
            for elem in elemList]


def printPath(problem: PathProblem, path: Path) -> None:
    points: "iter[Point]" = sum(map(lambda edge: (edge.to, edge.from_), problem.graph), ())

    xs: "tuple[int]" = tuple(map(lambda point: int(point.x), path.points))
    ys: "tuple[int]" = tuple(map(lambda point: int(point.y), path.points))

    for i in range(min(xs)-1, max(xs)+2):
        for j in range(min(ys)-1, max(ys)+2):
            point = Point(i, j)
            if problem.start == point:
                print("S", end="")
            elif problem.end == point:
                print("E", end="")
            elif point in path.points:
                print(".", end="")
            elif point in points:
                print(" ", end="")
            else:
                print("#", end="")
        print()


def printResult(title: str, problem: PathProblem, isGrid: bool = True) -> None:
    print(f"{title}\nfrom {problem.start} to {problem.end}")
    result: Path = shortestPath(problem, isGrid)
    if result.length():
        print(result.length())
        printPath(problem, result)
    else:
        print("no path found")
    print("\n\n")


def mainPath() -> None:
    printResult("grid", path("grid.txt"))
    printResult("spiral", path("spiral.txt"))
    printResult("bunker", path("bunker.txt"))
    printResult("line", path("line.txt"))
    printResult("Small hole", path("small_hole.txt"))
    printResult("Stick man", path("stickman.txt"))

    printResult("Simple graph 5x4 grid", PathProblem(shuffle(gridNorthEast(5, 4)), Point(0, 0), Point(3, 3)), False)
    printResult("Large graph 50x40 grid", PathProblem(shuffle(gridNorthEast(50, 40)), Point(0, 0), Point(30, 30)), False)
    printResult("Large graph  with cycle 50x40 grid", PathProblem(shuffle(gridFull(50, 40)), Point(0, 0), Point(30, 30)))
    # too long yet for mapping in printPath
    # printResult("Huge graph 200x300 grid", PathProblem(shuffle(gridNorthEast(200, 300)), Point(0, 0), Point(30, 30)), False)


def shuffle(grid: list) -> list:
    random.shuffle(grid)
    return grid


if __name__ == "__main__":
    mainPath()
