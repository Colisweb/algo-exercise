class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = float(x)
        self.y: float = float(y)

    def __str__(self) -> str:
        return f"{self.x}x{self.y}"

    def __eq__(self, other: object) -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def isNeighbor(self, other: object) -> bool:
        return (self.x == other.x and (self.y == other.y - 1 or self.y == other.y + 1)) or \
               (self.y == other.y and (self.x == other.x - 1 or self.x == other.x + 1))
