#from solutionCode import *
import itertools
import copy

def is_clique(S, G):
  # generate every pair
  for (a, b) in itertools.combinations(S, 2):
    # is this pair disconnected?
    if G[a][b] == 0:
      # disconnected - not a clique
      return False

  # all connected - a clique
  return True

def is_indset(S, G):
  # generate every pair
  for (a, b) in itertools.combinations(S, 2):
    # is this pair connecte?
    if G[a][b] == 1:
      # connected - not an independent set
      return False

  # none connected - an independent set
  return True

def complement(G):
  # copy the graph
  C = copy.deepcopy(G)

  # flip every value in the adjacency matrix
  for i in range(len(C)):
    for j in range(len(C)):
      # 1 - 1 = 0
      # 1 - 0 = 1
      C[i][j] = 1 - C[i][j]

  # flip the diagonal back
  # so that nodes are not connected
  # to themselves if they weren't before
  for i in range(len(C)):
    C[i][i] = 1 - C[i][i]

  # return the complement
  return C

def has_clique_at_least(G, k):
  for i in range(k, len(G)):
    for points in itertools.combinations(range(len(G)), i):
      if is_clique(list(points), G):
        return list(points)

  return False

def largest_clique(G):
  for i in range(len(G), 1, -1):
    for points in itertools.combinations(range(len(G)), i):
      if is_clique(list(points), G):
        return list(points)

  return None

ex1 = [
  [0, 1, 0, 0, 0, 0, 0],
  [1, 0, 1, 1, 0, 0, 0],
  [0, 1, 0, 1, 1, 1, 0],
  [0, 1, 1, 0, 1, 1, 0],
  [0, 0, 1, 1, 0, 1, 1],
  [0, 0, 1, 1, 1, 0, 1],
  [0, 0, 0, 0, 1, 1, 0]
]

ex1_comp = [
  [0, 0, 1, 1, 1, 1, 1],
  [0, 0, 0, 0, 1, 1, 1],
  [1, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 1],
  [1, 1, 0, 0, 0, 0, 0],
  [1, 1, 0, 0, 0, 0, 0],
  [1, 1, 1, 1, 0, 0, 0]
]

if __name__ == "__main__":
    # if you have not yet implemented one of the functions, comment out those tests
    assert is_clique([2,3,4,5], ex1) == True
    assert is_clique([1,2,3], ex1) == True
    assert is_clique([1,2,3,6], ex1) == False
    assert is_clique([0,1,5,6], ex1) == False
    assert is_clique([1,2,3,4], ex1) == False

    assert is_indset([1,3,5], ex1) == False
    assert is_indset([1,2,6], ex1) == False
    assert is_indset([3,6], ex1) == True
    assert is_indset([0,2,6], ex1) == True
    assert is_indset([0,3,], ex1) == True

    assert complement(ex1) == ex1_comp

    print(has_clique_at_least(ex1, 4))
    print(largest_clique(ex1))

    print("All tests passed!")
