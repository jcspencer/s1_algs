# BEST CASE: O(nlogn)
# WORST CASE: O(n^2)
def quicksort(lst):
  quicksort_inner(lst, 0, len(lst) - 1)
  return lst

def quicksort_inner(lst, low, high):
  # if still not sorted
  if low < high:
    p = partition(lst, low, high)

    # sort lower half
    quicksort_inner(lst, low, p - 1)
    # sort upper half
    quicksort_inner(lst, p + 1, high)

def partition(lst, low, high):
  # pick a pivot
  pivot = lst[high]
  i = low

  for j in range(low, high):
    # swap if item is lower than the pivot
    if lst[j] < pivot:
      lst[i], lst[j] = lst[j], lst[i]
      i += 1

  lst[i], lst[high] = lst[high], lst[i]
  return i

if __name__ == "__main__":
  print(quicksort([5,4,3,2,1]))
