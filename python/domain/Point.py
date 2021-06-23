class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y

    def __str__(self) -> str:
        return f"{self.x}x{self.y}"
