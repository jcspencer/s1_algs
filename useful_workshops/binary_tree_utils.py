def count(T, v):
  def inner(T, v):
    # deconstruct the given node into left and right
    (left, right) = T[v]

    # if the node if None, return 0
    # otherwise, return 1
    left_total = 1 if left else 0
    right_total = 1 if right else 0

    # if there is a child node on the left...
    if left:
      # recursively calculate the number of child nodes
      # the left node has
      l = inner(T, left)

      # add it to the total
      left_total += l

    # if there is a child node on the right...
    if right:
      # recursively calculate the number of child nodes
      # the right node has
      r = inner(T, right)

      # add it to the total
      right_total += r

    return left_total + right_total

  # caculate the number of nodes in the subtree
  # starting at node 'v'.
  # (We add 1 to include the parent node)
  return inner(T, v) + 1

def balance(T, v):
  # deconstruct the given node into left and right
  (left, right) = T[v]

  # if there is a left node, count the number of nodes on it's side
  l = count(T, left) if left else 0

  # if there is a right node, count the number of nodes on it's side
  r = count(T, right) if right else 0

  # compute the balance of the two child tree
  return l - r

def expecting(name, expected, actual):
  print(name)
  print("expecting:", expected)
  print("got:      ", actual)
  print()

if __name__ == "__main__":
  tree = [(2, 1), (3, None), (5, 4), (None, None), (None, None), (None, None)]

  expecting('count(tree, 0)', 6, count(tree, 0))
  expecting('count(tree, 1)', 2, count(tree, 1))
  expecting('count(tree, 2)', 3, count(tree, 2))
  expecting('count(tree, 4)', 1, count(tree, 4))

  expecting('balance(tree, 0)', 1, balance(tree, 0))
