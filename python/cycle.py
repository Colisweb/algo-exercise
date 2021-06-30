from domain.Point import Point
from domain.Edge import Edge
from domain.Path import Path
import numpy as np
from sys import float_info


def shortCycle(points: "list[Point]") -> Path:
    # np.random.seed(0)
    generated = looper(points, lambda points: [points[0]] + algoProba(points[1:], points[0]) + [points[0]])
    straightened = looper(generated, lambda points: straightener(points), best=Path(generated).length(), associated=generated)
    uncrossed = uncrosser(straightened)
    return Path(uncrossed)


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


def uncrosser(points: "list[Point]", currentPos: int = 0) -> "list[Point]":
    if currentPos + 2 > len(points):
        return points

    currentSegment = Edge(points[currentPos], points[currentPos + 1])
    cutted = [(id, Edge(point, points[id + 1])) for id, point in enumerate(points) if currentSegment.cross(Edge(point, points[id + 1]))]
    # cutted = [Edge(point, points[currentPos + id + 1]) for id, point in enumerate(points[currentPos + 1:]) if Edge(point, points[currentPos + id + 1]).cross(currentSegment)]

    if len(cutted) == 1:
        nextSegment = Edge(points[currentPos + 1], points[currentPos + 2])
        nextCutted = [edge for _, edge in cutted if nextSegment.cross(edge)]

        index = cutted[0][0]

        if len(nextCutted) == 1:
            if index < currentPos:
                index -= 1
            points.insert(index, points.pop(currentPos + 1))

        else:
            if index < currentPos:
                begin = index + 1
                end = currentPos
            else:
                begin = currentPos + 1
                end = index
            points[begin:end] = points[begin:end:-1]

    return uncrosser(points, currentPos + 1)
