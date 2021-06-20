from Point import Point


class Path:
    def __init__(self, points: "list[Point]" = []):
        self.points = points

    def length(self) -> float:
        return 0  # calcul de la distance euclidienne ici?
