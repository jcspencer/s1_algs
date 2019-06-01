from math import inf
from collections import deque

def bfs_traversal(graph, s):
  visited = []
  boundary = deque([s])

  while len(boundary) > 0:
    v = boundary.popleft()
    visited += [v]
    for u in neighbours(v, graph):
      if u not in visited and u not in boundary:
        boundary.append(u)

  return visited

def bfs_distances(graph, s):
  dists= [inf] * len(graph)
  dists[s] = 0
  visited = []
  boundary = deque([s])

  while len(boundary) > 0:
    v = boundary.popleft()
    visited += [v]
    for u in neighbours(graph, v):
      if u not in visited and u not in boundary:
        boundary.append(u)
        dists[u] = dists[v] + 1

  return dists

def neighbours(graph, v):
  verticies = range(0, len(graph))
  connected = graph[v]
  m = [a * b for a, b in zip(verticies, connected)]

  return list(filter(lambda x: x != 0, m))

