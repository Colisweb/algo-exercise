from domain.Point import Point
from domain.Edge import Edge
from domain.Path import Path
import numpy as np
from sys import float_info


def shortCycle(points: "list[Point]") -> Path:
    # np.random.seed(0)
    generated = looper(points, lambda points: [points[0]] + algoProba(points[1:], points[0]))
    optimized = looper(generated, lambda points: straightener(points), best=Path(generated).length(), associated=generated)
    return Path(optimized)


def looper(points: "list[Point]", method, tries: int = 20, best: float = float_info.max, associated: "list[Point]" = None) -> "list[Point]":
    path = Path(method(points))
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

    distances = [1 / Edge(current, pt).distance() if current != pt else 0 for pt in newPoints[:10]][::-1]
    max = sum(distances)
    percentages = [sum(distances[:id + 1]) / max for id in range(len(distances))]

    # randVal = random.uniform(0, 1)
    randVal = np.random.beta(5, 2)  # plus proche de 1 que de 0

    index = np.searchsorted([val > randVal for val in percentages], True, side='left') + 1
    # print(f"found index as {index:2}", end=", ")
    index = len(percentages) - index
    # print(f"convert it to {index:2}", end=" => ")

    # print(f"{index:2} on {len(newPoints):2} is ", end="")
    # print(newPoints[index])

    # tmp : à débuger
    if index == len(newPoints):
        index -= 1
    if index > len(newPoints):
        index -= 2

    selected = newPoints.pop(index)

    return [selected] + algoProba(newPoints, selected)


def straightener(points: "list[Point]", currentPos: int = 0) -> "list[Point]":
    if currentPos + 4 > len(points):
        return points

    currentWindow = points[currentPos:currentPos + 4]

    if Path(currentWindow).length() > Path([currentWindow[0], currentWindow[2], currentWindow[1], currentWindow[3]]).length():
        points[currentPos + 1] = currentWindow[2]
        points[currentPos + 2] = currentWindow[1]

    return straightener(points, currentPos + 1)
