def dijkstra(graph, s):
  dist = [inf]*len(graph)
  dist[s] = 0
  visited = []
  boundary = [s]
  while len(boundary) > 0:
    v = extract_min(boundary, dist)
    visited += [v]
    for u in neighbours(v, graph):
      if dist[u] == inf:
        boundary.append(u)
    alt = dist[v] + graph[v][u]
    dist[u] = min(dist[u], alt)

  return dst
