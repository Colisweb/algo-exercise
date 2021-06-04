package com.colisweb.exercise.domain

final case class Path(points: List[Point] = Nil) {
  lazy val length: Double = ???
}
