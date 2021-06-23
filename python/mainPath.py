from domain.Point import Point
from domain.Path import Path
from domain.PathProblem import PathProblem
from parsing.readFromResources import path
from shortestPath import shortestPath
import random


def printPath(problem: PathProblem, path: Path) -> None:
    points: "list[Point]" = list(set(map(lambda edge: [Point(edge.to.x, edge.to.y), Point(edge.from_.x, edge.from_.y)], problem.graph)))
    # points: "list[Point]" = list(set(map(lambda edge: [edge.to, edge.from_], problem.graph)))

    xs: "list[int]" = map(lambda point: point.x, path.points)
    ys: "list[int]" = map(lambda point: point.y, path.points)

    for i in range(min(xs)-1, max(xs)+1):
        for j in range(min(ys)-1, max(ys)+1):
            point = Point(i, j)
            if problem.start == point:
                print("S")
            elif problem.end == point:
                print("E")
            elif point in path.points:
                print(".")
            elif point in points:
                print(" ")
            else:
                print("#")
        print()


def printResult(title: str, problem: PathProblem) -> None:
    print(f"{title}\nfrom {problem.start} to {problem.end}")
    result: Path = shortestPath(problem)
    if result: # verify monad
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
