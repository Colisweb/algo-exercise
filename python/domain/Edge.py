from .Point import Point
from math import sqrt
# all from https://stackoverflow.com/questions/33672412/python-functools-lru-cache-with-class-methods-release-object
# from methodtools import lru_cache  # specific for class methods ? seems intern to instance
# from ring import lru  # seems to works as above but with sharing among all classes instances
# from functools import cached_property  # 3.8 specific, should works as lru cache...

# from functools import lru_cache  # else


class Edge:
    def __init__(self, from_: Point, to: Point) -> None:
        self.from_: Point = from_
        self.to: Point = to

    def __str__(self) -> str:
        return f"{self.from_}-{self.to}"

    def __eq__(self, other: object) -> bool:
        return self.from_ == other.from_ and self.to == other.to

    def __hash__(self) -> int:
        return hash((self.from_, self.to))

    def _sqr(self, d: float) -> float:
        return d**2

    def _distance2(self) -> float:
        return self._sqr(self.from_.x - self.to.x) + self._sqr(self.from_.y - self.to.y)

    def distance(self) -> float:
        return sqrt(self._distance2())
