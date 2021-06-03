
scalaVersion := "2.13.5"

ThisBuild / scalafmtCheck := true
ThisBuild / scalafmtSbtCheck := true

ThisBuild / pushRemoteCacheTo := Some(
  MavenCache("local-cache", baseDirectory.value / sys.env.getOrElse("CACHE_PATH", "sbt-cache"))
)
ThisBuild / isSnapshot := true



libraryDependencies ++= Seq(
)

Global / onChangedBuildSource := ReloadOnSourceChanges

ThisBuild / scalafmtOnCompile := true
ThisBuild / scalafmtCheck := true
ThisBuild / scalafmtSbtCheck := true

