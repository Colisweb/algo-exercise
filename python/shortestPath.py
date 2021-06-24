from domain.Path import Path
from domain.Point import Point
from domain.PathProblem import PathProblem


def shortestPath(pathProblem: PathProblem) -> Path:  # wrap into monad
    return Path([Point(0, 0), Point(10, 10)])  # TODO: add algorithm
