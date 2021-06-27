from domain.Point import Point
from domain.Edge import Edge
from domain.Path import Path
import random
import numpy as np


def shortCycle(points: "list[Point]") -> Path:
    # np.random.seed(0)
    return Path(looper(points, lambda points: Path([points[0]] + algoProba(points[1:], points[0]))))


# straightener : take "4 points windows" and try to swap the 2nd and the 3rd


def looper(points: "list[Point]", method, tries: int = 10, best: float = 10000, associated: Path = None) -> "list[Point]":
    path = method(points)
    length = path.length()

    if length < best:
        best = length
        associated = path.points

    if not tries:
        return associated

    return looper(points, method, tries - 1, best, associated)


def algoProba(points: "list[Point]", current: Point) -> "list[Point]":
    if len(points) == 1:
        return points

    newPoints = sorted(points, key=lambda pt: Edge(current, pt).distance())

    distances = [1 / Edge(current, pt).distance() for pt in newPoints][::-1]
    max = sum(distances)
    percentages = [sum(distances[:id + 1]) / max for id in range(len(distances))]

    # randVal = random.uniform(0, 1)
    randVal = np.random.beta(5, 2)  # plus proche de 1 que de 0

    index = len(percentages) - np.searchsorted([val > randVal for val in percentages], True, side='left') + 1

    # tmp : à débuger
    if index == len(newPoints):
        index -= 1
    if index > len(newPoints):
        index -= 2

    selected = newPoints.pop(index)

    return [selected] + algoProba(newPoints, selected)
