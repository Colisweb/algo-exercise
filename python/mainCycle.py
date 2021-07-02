from domain.Point import Point
from domain.Path import Path
from parsing.readFromResources import cycle
from shortestCycle import shortestCycle

from sys import argv
import random
import numpy as np
from functools import lru_cache
import matplotlib.pyplot as plt


def mainCycle() -> None:
    try:
        seed = float(argv[1])
        np.random.seed(seed)
        random.seed(seed)
    except Exception:
        pass

    shortestCycle(pointsInGrid(10, 8))

    print("80 points in a 8x10 grid")
    printResult(shortestCycle(shuffle(pointsInGrid(10, 8))))

    # take 40ms to generate only
    # print("200 random points")
    # printResult(shortestCycle(shuffle([val for liste in [pointsInGrid(random.randint(0, 700), random.randint(0, 700)) for _ in range(200)] for val in liste])))

    print("File 14 nodes")
    printResult(shortestCycle(cycle("14_nodes.txt")))

    print("File 52 nodes")
    printResult(shortestCycle(cycle("52_nodes.txt")))

    print("File 202 nodes")
    printResult(shortestCycle(cycle("202_nodes.txt")))

    # more than 1000 depth recursion allowed by python
    # print("File 1002 nodes")
    # printResult(shortestCycle(cycle("1002_nodes.txt")))

    # print("File 5915 nodes")
    # printResult(shortestCycle(cycle("5915_nodes.txt")))


@lru_cache()
def pointsInGrid(width: int, height: int) -> "list[Point]":
    return [Point(x, y) for x in range(width) for y in range(height)]


def shuffle(grid: list) -> list:
    random.shuffle(grid)
    return grid


def printResult(path: Path) -> None:
    length = f"{path.length():,.4f}"
    print(f"{length}\n{','.join(map(lambda x: str(x), path.points[::-1]))}\n\n")

    xs: "list[float]" = tuple(map(lambda point: point.x, path.points))
    ys: "list[float]" = tuple(map(lambda point: point.y, path.points))
    plt.plot(xs, ys, c='orange')
    # plt.scatter(xs[1:-1], ys[1:-1], c='red', marker='.')
    # plt.scatter(xs[0], ys[0], c='blue', marker='.')
    plt.title(length)
    plt.show()


if __name__ == "__main__":
    mainCycle()
