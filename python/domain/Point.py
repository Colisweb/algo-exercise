class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def toString(self) -> str:
        return f"{self.x}x{self.y}"
