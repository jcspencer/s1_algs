# O(n)
def min_index(lst):
  m = 0

  # Keep searching for the lowest item
  for i in range(len(lst)):
    if lst[i] < lst[m]:
      m = i

  # Return the index of the lowest item
  return m

# BEST CASE: O(n^2)
# WORST CASE: O(n^2)
def selection_sort(lst):
  # iterate over every item
  for i in range(len(lst)):
    # get the index of the lowest item in
    # the unsorted portion of the list
    j = min_index(lst[i:]) + i

    # swap the current item and the lowest
    # in the remainder of the list
    lst[i], lst[j] = lst[j], lst[i]

  return lst

if __name__ == "__main__":
  print(selection_sort([5,4,3,2,1]))
