from domain.Point import Point
from domain.Edge import Edge
from domain.Path import Path
import random
import numpy as np


def shortCycle(points: "list[Point]") -> Path:
    return Path(algoProba(points[1:], points[0]))


def algoProba(points: "list[Point]", current: Point) -> "list[Point]":
    if len(points) == 1:
        return points

    # ordonne les points restants par distance
    newPoints = sorted(points, key=lambda pt: Edge(current, pt).distance())

    # transforme list en suite mathématiques
    distances = [1 / Edge(current, pt).distance() for pt in newPoints][::-1]
    max = sum(distances)
    percentages = [sum(distances[:id + 1]) / max for id in range(distances)]

    # fait tirage au sort
    randVal = random.randint(0, 100)

    # prend premier point de valeur > à tirage
    index = len(newPoints) - np.searchsorted([val > randVal for val in percentages], True, side='left')

    selected = newPoints.pop(index)

    return [selected] + algoProba(newPoints, selected)
