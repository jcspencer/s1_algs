# helper method calling quicksort
# with default low and high values
def quicksort(lst):
  quicksort_inner(lst, 0, len(lst) - 1)
  return lst

def quicksort_inner(lst, low, high):
  if low < high:
    p = partition(lst, low, high)

    # sort lower half
    quicksort_inner(lst, low, p - 1)
    # sort upper half
    quicksort_inner(lst, p + 1, high)

def partition(lst, low, high):
  pivot = lst[high]
  i = low
  for j in range(low, high):
    if lst[j] < pivot:
      lst[i], lst[j] = lst[j], lst[i]
      i += 1
  lst[i], lst[high] = lst[high], lst[i]
  return i

def expecting(name, expected, actual):
  print(name)
  print("expecting:", expected)
  print("got:      ", actual)
  print()

if __name__ == "__main__":
  lst = [5, 4, 3, 2, 1]

  expecting('quicksort([5, 4, 3, 2, 1])', [1, 2, 3, 4, 5], quicksort(lst))
