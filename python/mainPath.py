from domain.Point import Point
from domain.Path import Path
from domain.PathProblem import PathProblem
from parsing.readFromResources import path
from shortestPath import shortestPath
import random


def printPath(problem: PathProblem, path: Path) -> None:
    points: "list[Point]" = sum(map(lambda edge: (edge.to, edge.from_), problem.graph), ())

    xs: "list[int]" = tuple(map(lambda point: point.x, path.points))
    ys: "list[int]" = tuple(map(lambda point: point.y, path.points))

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


def printResult(title: str, problem: PathProblem) -> None:
    print(f"{title}\nfrom {problem.start} to {problem.end}")
    result: Path = shortestPath(problem)
    if result.length():
        print(result.length())
        printPath(problem, result)
    else:
        print("no path found")
    print("\n\n")


def mainPath() -> None:
    # seed = args, from str to float
    # random.seed()

    printResult("grid", path("grid.txt"))
    printResult("spiral", path("spiral.txt"))
    printResult("bunker", path("bunker.txt"))
    printResult("line", path("line.txt"))
    printResult("Small hole", path("small_hole.txt"))
    printResult("Stick man", path("stickman.txt"))

    # todo : finish here + functions


if __name__ == "__main__":
    mainPath()
