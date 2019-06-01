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
  connected = graph[v]
  n = []

  for index, c in enumerate(connected):
    if c:
      # this vertex is connected to 'v',
      # so we add it to the list
      n.append(index)

  return n
