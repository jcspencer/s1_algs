# insert an undirectional edge from
# vertex 'i' to 'j'
def insert_edge(graph, i, j):
  graph[i][j] = 1
  graph[j][i] = 1

# check if a specfic edge exists
def edge_exists(graph, i, j):
  return graph[i][j] == 1

def extension(connected, graph):
  n = len(graph)
  for i in connected:
    for j in range(n):
      if j not in connected and edge_exists(graph, i, j):
          return i, j

def spanning_tree(graph):
  n = len(graph)
  tree = empty_graph(n)
  r = random.randrange(0, n)
  connected = [r]

  while len(connected) < n:
    i, j = extension(connected, graph)
    insert_edge(tree, i, j)
    connected += [j]

  return tree
