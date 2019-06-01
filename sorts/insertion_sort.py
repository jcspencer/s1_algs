# BEST CASE: O(n)
# WORST CASE: O(n^2)
def insertion_sort(lst):
  # iterate over every item in the list
  for l in range(1, len(lst)):
    i = l

    # keep swapping lst[l] back until
    # it's in the rigt order
    # BEST CASE: never run
    # WORSE CASE: run 'n' times
    while i > 0 and lst[i - 1] > lst[i]:
      lst[i], lst[i - 1] = lst[i - 1], lst[i]
      i -= 1

  return lst

if __name__ == "__main__":
  print(insertion_sort([5,4,3,2,1]))
