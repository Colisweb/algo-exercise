from .Point import Point
from math import sqrt


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

    def _equation(self) -> "tuple[float, float]":
        m = (self.to.y - self.from_.y) / ((self.to.x - self.from_.x) if self.from_.x != self.to.x else 0.01)
        b = self.to.y - m * self.to.x
        return m, b

    def cross(self, other: object) -> bool:
        if self == other:
            return False

        mSelf, bSelf = self._equation()
        mOther, bOther = other._equation()

        if mSelf == mOther:
            return False

        x = (bOther - bSelf) / (mSelf - mOther)
        y = mSelf * x + bSelf

        return ((min(self.from_.x, self.to.x) < x < max(self.from_.x, self.to.x) and
                 min(other.from_.x, other.to.x) < x < max(other.from_.x, other.to.x)) or
                (min(self.from_.y, self.to.y) < y < max(self.from_.y, self.to.y) and
                 min(other.from_.y, other.to.y) < y < max(other.from_.y, other.to.y)))
