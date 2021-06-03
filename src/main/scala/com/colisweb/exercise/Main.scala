package com.colisweb.exercise

object Main extends App {
  val simple = Set.tabulate(5, 3) { case (x, y) =>
    Set(
      Edge(from = Point(x, y), to = Point(x + 1, y)),
      Edge(from = Point(x, y), to = Point(x, y + 1)),
      Edge(from = Point(x, y), to = Point(x + 1, y + 1))
    )
  }.flatten.flatten
  val result = ShortestPath.shortestPath(graph = simple, start = Point(0, 0), end = Point(3, 3))

}
