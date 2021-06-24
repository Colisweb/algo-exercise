from domain.Point import Point
from domain.Path import Path
from parsing.readFromResources import cycle
from cycle import shortCycle
import random


def pointsInGrid(width: int, height: int) -> "list[Point]":
    return [Point(x, y) for x in range(width) for y in range(height)]


def printResult(path: Path) -> None:
    print(f"{path.length()}\n{','.join(path.points[::-1])}\n\n")


def mainCycle() -> None:
    # seed = args, from str to float
    # random.seed()

    shortCycle(iter(pointsInGrid(10, 8)))

    print("80 points in a 8x10 grid")
    grid = pointsInGrid(10, 8)
    random.shuffle(grid)
    printResult(shortCycle(iter(grid)))

    return  # secu

    # print("200 random points")
    # grid = [pointsInGrid(random.randint(0, 700), random.randint(0, 700)) for _ in range(200)]
    # random.shuffle(grid)
    # printResult(shortCycle(iter(grid)))

    # print("File 14 nodes")
    # printResult(shortCycle(iter(cycle("14_nodes.txt"))))

    # print("File 52 nodes")
    # printResult(shortCycle(iter(cycle("52_nodes.txt"))))

    # print("File 202 nodes")
    # printResult(shortCycle(iter(cycle("202_nodes.txt"))))

    # print("File 1002 nodes")
    # printResult(shortCycle(iter(cycle("1002_nodes.txt"))))

    # print("File 5915 nodes")
    # printResult(shortCycle(iter(cycle("5915_nodes.txt"))))


if __name__ == "__main__":
    mainCycle()
