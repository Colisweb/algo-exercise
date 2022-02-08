from .Point import Point
from .Edge import Edge


class PathProblem:
    def __init__(self, graph: "list[Edge]", start: Point, end: Point) -> None:
        self.graph: "list[Edge]" = graph
        self.start: Point = start
        self.end: Point = end
