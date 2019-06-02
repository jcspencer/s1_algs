def safe(graph, vertex, pos, path):
  # check if current vertex and
  # last vertex in path are adjacent 
  if graph[path[pos-1]][vertex] == 0:
    return False

  # check the current vertex is not already
  # in the path
  for v in path:
    if v == vertex:
      return False

  return True

def ham_cycle_inner(graph, pos, path):
  # all verticies are in the path, no need to recurse
  if pos == len(graph):
    # it's actually a cycle
    if graph[path[pos-1]][path[0]] == 1:
      return True
    else:
      return False

  # try other verticies as canididates
  for v in range(1, len(graph)):
    if safe(graph, v, pos, path):
      # make the move
      path[pos] = v

      # test the move out
      if ham_cycle_inner(graph, pos + 1, path):
        return True

      # move wasn't successful, revert it
      path[pos] = -1

  return False

def ham_cycle(graph):
  path = [-1] * len(graph)
  path[0] = 0

  result = ham_cycle_inner(graph, 1, path)

  if result:
    print('found a result:')
    print(path)
  else:
    print('no result found:')

if __name__ == "__main__":
  g = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
  ]

  print(ham_cycle(g))
