def left_child(i):
  return 2*i

def right_child(i):
  return 2*i + 1

def parent(i):
  return i // 2

def is_leaf(heap, i):
  n = len(heap) - 1
  return (i >= (n/2)) and (i <= n)

def min_child(heap, i):
  n = len(heap) - 1

  # indexes of children
  left = left_child(i)
  right = right_child(i)

  # no children
  if (left > n or heap[left] is None) and (right > n or heap[left] is None):
    return None

  # only a right child
  if (left > n or heap[left] is None):
    return right

  # only a left child
  if (right > n or heap[right] is None):
    return left

  # two children, get the smallest one
  if heap[left] > heap[right]:
    return right
  else:
    return left

def insert(heap, item):
  # put it at the end
  heap.append(item)

  # swap up
  n = len(heap) - 1
  current = n
  while heap[current] < heap[parent(current)]:
    heap[current], heap[parent(current)] = heap[parent(current)], heap[current]
    current = parent(current)

def min_heapify(heap, root):
  if not is_leaf(heap, root):
    # not two children?
    if left_child(root) > (len(heap) - 1) or right_child(root) > (len(heap) - 1):
      return

    # if heap needs to be moved down
    if heap[root] > heap[left_child(root)] or heap[root] > heap[right_child(root)]:
      # find the min child
      m = min_child(heap, root)
      if m:
        # swap down
        heap[root], heap[m] = heap[m], heap[root]
        # recurse from here
        min_heapify(heap, m)

def extract_min(heap):
  # pull the root node
  ret = heap[1]
  # swap first and last
  heap[1] = heap[-1]
  # remove last
  heap.pop()
  # fix up the heap
  min_heapify(heap, 1)
  # return the root node we popped
  return ret

# BEST CASE: O(nlogn)
# WORST CASE: O(nlogn)
def heapsort(lst):
  # create an empty heap and fill it
  heap = [0]
  for item in lst:
    insert(heap, item)

  # fix up the heap if need be
  min_heapify(heap, 1)

  out = []

  # repeatedly remove the min item from the heap
  while len(heap) > 1:
    out.append(extract_min(heap))

  return out

if __name__ == "__main__":
  print(heapsort([5,4,3,2,1]))

