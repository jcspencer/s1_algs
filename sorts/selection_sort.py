def min_index(lst):
  m = 0

  for i in range(len(lst)):
    if lst[i] < lst[m]:
      m = i

  return m

def selection_sort(lst):
  for i in range(len(lst)):
      sliced = lst[i:]
      j = min_index(sliced) + i
      lst[i], lst[j] = lst[j], lst[i]

  return lst
