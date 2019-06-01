def insertion_sort(lst):
  for l in range(1, len(lst)):
    i = l
    while i > 0 and lst[i - 1] > lst[i]:
      lst[i], lst[i - 1] = lst[i - 1], lst[i]
      i -= 1

  return lst
