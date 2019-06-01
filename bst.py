# node = (key, left, right)

def search(node, key):
  # there is no tree
  if node is None:
    return None

  # decompose the current node
  (k, l, r) = node

  if k == key:
    # found it
    return node
  elif key < k:
    # go left
    return search(l, key)
  else:
    # go right
    return search(r, key)

def insert(node, key):
  # if a node doesn't exist,
  # build a new leaf node
  if node is None:
    return (key, None, None)

  # decompose the current node
  (k, l, r) = node

  if key == k:
    # replace the key in the current node
    return (key, l, r)
  elif key < k:
    # insert to the left
    left = insert(l, key)
    return (k, left, r)
  else:
    # insert to the right
    right = insert(r, key)
    return (k, l, right)

def find_min(root):
  current = root
  # keep going to the left
  while current is not None and current[1]:
    current = current[1]
  return current

def delete(node, key):
  if node is None:
    return None

  # decompose root node
  (k, l, r) = node

  if key < k:
    # key to be deleted lies in the left subtree
    return (k, delete(l, key), r)
  elif key > k:
    # key to be deleted lies in the right subtree
    return (k, l, delete(r, key))
  else:
     # the node we want to delete is this node

     # node with 0, 1 chuildren
     if l is None:
        return r
     elif r is None:
         return l

     # two children, get the inorder successor
     (temp_key, _, _) = find_min(r)
     left = l

     # delete the in-order successor
     right = delete(r, temp_key)

     # copy the inorder successors key to the root
     # and return the new tree
     return (temp_key, left, right)
