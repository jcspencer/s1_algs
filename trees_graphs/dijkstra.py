from math import inf
import heapq

def dijkstra(graph, s):
  # initialise all the lengths to infinity
  dist = [inf]*len(graph)

  # the distance from s to itself is 0
  dist[s] = 0

  # what nodes have we visited
  visited = []

  # all nodes initially unexplored
  # (this is a min-priority queue)
  boundary = [(0, s)]
  while len(boundary) > 0:
    # get the node with the minimum distance
    _, v = heapq.heappop(boundary)

    # add this node to the visited list
    visited += [v]

    # iterate over this nodes neighbours
    for u in neighbours(graph, v):
      # if the distance was prevously unknown,
      # add it to the boundary fronteir
      if dist[u] == inf:
        # (priority, value)
        heapq.heappush(boundary, (dist[u], u))

      # get the length of this path
      alt = dist[v] + graph[v][u]

      # check if this path is better than what we
      # already had
      dist[u] = min(dist[u], alt)

  return dist

def neighbours(graph, v):
  connected = graph[v]
  n = []

  for index, c in enumerate(connected):
    if c:
      n.append(index)

  return n

g = [
  [0, 3, 3, 0, 0, 0],
  [3, 0, 5, 0, 0, 0],
  [3, 5, 0, 11, 1, 0],
  [0, 0, 11, 0, 11, 5],
  [0, 0, 1, 11, 0, 7],
  [0, 0, 0, 5, 7, 0]
]

print(dijkstra(g, 0))
