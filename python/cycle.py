from domain.Point import Point
from domain.Edge import Edge
from domain.Path import Path
import numpy as np
from sys import float_info
import matplotlib.pyplot as plt


def saveGraph(points, nom):
    path = Path(points)
    xs: "list[float]" = tuple(map(lambda point: point.x, path.points))
    ys: "list[float]" = tuple(map(lambda point: point.y, path.points))
    plt.plot(xs, ys, c='orange')
    plt.scatter(xs[1:-1], ys[1:-1], c='red', marker='x')
    plt.scatter(xs[0], ys[0], c='blue', marker='o')
    plt.title(f"{path.length():,.4f}")
    plt.savefig(nom)
    plt.clf()


def shortCycle(points: "list[Point]") -> Path:
    # np.random.seed(0)
    # generated = looper(points, lambda points: [points[0]] + algoProba(points[1:], points[0]) + [points[0]])
    generated = [Point(16.47, 96.1), Point(17.2, 96.29), Point(16.53, 97.38), Point(16.3, 97.38), Point(14.05, 98.12), Point(19.41, 97.13), Point(20.47, 97.02), Point(22.0, 96.05), Point(21.52, 95.59), Point(20.09, 94.55), Point(20.09, 92.54), Point(22.39, 93.37), Point(25.23, 97.24), Point(16.47, 94.44), Point(16.47, 96.1)]

    saveGraph(generated, "generated")
    straightened = looper(generated, lambda points: straightener(points), tries=2, best=Path(generated).length(), associated=generated.copy())
    saveGraph(straightened, "straightened")
    uncrossed = looper(straightened, lambda points: uncrosser(points), tries=2, best=Path(straightened).length(), associated=straightened.copy())
    # print([str(point) for point in uncrossed])
    saveGraph(uncrossed, "uncrossed")
    exit()
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

    # id points 4-5 et 11-12

    currentSegment = Edge(points[currentPos], points[currentPos + 1])
    # print("\n\ncurrent segment: id ", currentPos, currentPos + 1, " coords ", str(currentSegment))
    cutted = [(id + currentPos + 2, Edge(point, points[id + currentPos + 3])) for id, point in enumerate(points[currentPos + 2:-1]) if currentSegment.cross(Edge(point, points[id + currentPos + 3]))]

    # print([(id, id + 1, str(Edge(points[id], points[id + 1]))) for id, _ in cutted])
    if len(cutted) == 1:
    #     if currentPos + 3 > len(points):
    #         nextSegment = Edge(points[currentPos + 1], points[currentPos + 2])
    #         nextCutted = [edge for _, edge in cutted if nextSegment.cross(edge)]
    #     else:
    #         nextCutted = []

        index = cutted[0][0]
        # print(index)

    #     if len(nextCutted) == 1:
    #         if index < currentPos:
    #             index -= 1
    #         points.insert(index, points.pop(currentPos + 1))

    #     else:
        if index < currentPos:
            begin = index + 1
            end = currentPos
        else:
            begin = currentPos + 1
            end = index
        end += 1
        # print(begin, end - 1)
        points[begin:end] = points[begin:end][::-1]

    return uncrosser(points, currentPos + 1)
