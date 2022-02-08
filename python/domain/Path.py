from .Point import Point
from .Edge import Edge


class Path:
    def __init__(self, points: "list[Point]" = []) -> None:
        self.points: "list[Point]" = points

    def length(self) -> float:
        return 0 if len(self.points) < 2 else Edge(self.points[0], self.points[1]).distance() + Path(self.points[1:]).length()
