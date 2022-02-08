# Subject

## Introduction

In this exercise, you will implement 2 algorithms around the same kind of concepts (points, distances …) that we use at ***.


You are provided with a basic Scala program which runs the algorithms on several datasets. We expect a reasonable response time.


If Scala doesn’t suit you, you can use your preferred language, but we appreciate a lot:
- A functional style (no mutation of variables, recursion over iteration …)
- A functional language (Scala, Haskell, Caml …)
- Unit tests

Your program should run with the provided inputs.

## Algorithms
Tip: don’t reinvent the wheel! You can look for existing algorithms.

### Shortest path
Implement an algorithm that returns the shortest path from a set of points, a starting and an ending point.

Input:
- N points (x, y)
- M edges (one edge connects two points)
- Start point
- End point

Output:
- Set of edges that makes the path, starting with the start point and ending with the end point
- Distance travelled (euclidian)


### Shortest hamiltonian cycle
Implement an algorithm that returns a path as short as possible which visits every given point once, starting and ending at the same point (hamiltonian cycle).


Input:
- N points (x, y)

Output:
- Path using the N points
- Distance travelled (use the euclidean distance).


# Instructions

Once you have installed [sbt](https://www.scala-sbt.org/) to your machine, run

    sbt runMain com.colisweb.exercise.MainCycle 123

or

    sbt runMain com.colisweb.exercise.MainPath 123


The last argument is an optional seed so the scenario is reproductible.



