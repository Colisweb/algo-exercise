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
    generated = looper_generate(points, lambda points: [points[0]] + algoProba(points[1:], points[0]) + [points[0]], tries=5)

    # saveGraph(generated, "A generated")

    optimized = looper_global_opti(generated)
    # saveGraph(optimized, "A optimized")

    # exit()
    return Path(optimized)


def looper_generate(points: "list[Point]", method, tries: int = 20, best: float = float_info.max, associated: "list[Point]" = None) -> "list[Point]":
    path = Path(method(points))
    length = path.length()

    if length < best:
        best = length
        associated = path.points

    if not tries:
        return associated

    return looper_generate(points, method, tries - 1, best, associated)


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


def looper_global_opti(points: "list[Point]", best: float = float_info.max, associated: "list[Point]" = None) -> "list[Point]":
    uncrossed = looper_optimize(points, lambda pts: uncrosser(pts), best=Path(points).length(), associated=points.copy())
    smallWindow = looper_optimize(uncrossed, lambda pts: straightener(pts), best=Path(uncrossed).length(), associated=uncrossed.copy())
    largeWindow = looper_optimize(smallWindow, lambda pts: wideStraightener(pts), best=Path(smallWindow).length(), associated=smallWindow.copy())

    length = Path(largeWindow).length()

    if length < best:
        return looper_global_opti(largeWindow, length, largeWindow)

    return associated


def looper_optimize(points: "list[Point]", method, best: float = float_info.max, associated: "list[Point]" = None) -> "list[Point]":
    path = Path(method(points))
    length = path.length()

    if length < best:
        return looper_optimize(points, method, length, path.points)

    return associated


def uncrosser(points: "list[Point]", currentPos: int = 0) -> "list[Point]":
    if currentPos + 2 > len(points):
        return points

    currentSegment = Edge(points[currentPos], points[currentPos + 1])
    cutted = [(id + currentPos + 2, Edge(point, points[id + currentPos + 3])) for id, point in enumerate(points[currentPos + 2:-1]) if currentSegment.cross(Edge(point, points[id + currentPos + 3]))]

    if currentPos > 1:
        cutted += [(id, Edge(point, points[id + 1])) for id, point in enumerate(points[:currentPos - 2]) if currentSegment.cross(Edge(point, points[id + 1]))]

    if len(cutted) == 1:
        if currentPos + 2 > len(points) and cutted[0][1].cross(Edge(points[currentPos + 1], points[currentPos + 2])):
            points.insert(cutted[0][0], points.pop(currentPos + 1))

        else:
            index = cutted[0][0]

            if index < currentPos:
                begin = index + 1
                end = currentPos
            else:
                begin = currentPos + 1
                end = index
            end += 1

            points[begin:end] = points[begin:end][::-1]

    elif len(cutted) == 2 and cutted[0][0] + 1 == cutted[1][0]:
        points.insert(cutted[0][0] + 1, points.pop(currentPos + 1))

    return uncrosser(points, currentPos + 1)


def straightener(points: "list[Point]", currentPos: int = 0) -> "list[Point]":
    if currentPos + 4 > len(points):
        return points

    currentWindow = points[currentPos:currentPos + 4]

    if Path(currentWindow).length() > Path([currentWindow[0], currentWindow[2], currentWindow[1], currentWindow[3]]).length():
        points[currentPos + 1] = currentWindow[2]
        points[currentPos + 2] = currentWindow[1]

    return straightener(points, currentPos + 1)


def wideStraightener(points: "list[Point]", currentPos: int = 0) -> "list[Point]":
    if currentPos + 5 > len(points):
        return points

    currentWindow = points[currentPos:currentPos + 5]

    combination = [[currentWindow[1], currentWindow[2], currentWindow[3]],
                   [currentWindow[1], currentWindow[3], currentWindow[2]],
                   [currentWindow[2], currentWindow[1], currentWindow[3]],
                   [currentWindow[2], currentWindow[3], currentWindow[1]],
                   [currentWindow[3], currentWindow[1], currentWindow[2]],
                   [currentWindow[3], currentWindow[2], currentWindow[1]]]

    best = sorted(combination, key=lambda comb: Path([currentWindow[0]] + comb + [currentWindow[4]]).length())[0]

    points[(currentPos + 1)] = best[0]
    points[(currentPos + 2)] = best[1]
    points[(currentPos + 3)] = best[2]

    return wideStraightener(points, currentPos + 1)
