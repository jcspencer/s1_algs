def recursive_binary_search(a_list, target, low, high):
  # make sure the list is sorted
  a_list = sorted(a_list)

  def recursion(first, last):
    # find the middle index of the segment
    # we're searching in
    mid = (first + last) // 2

    if first > last:
      # not allowed
      return None
    elif (a_list[mid] < target):
      # item is greater than the middle,
      # so we only need to look at the right
      # half of the current list
      return recursion(mid + 1, last)
    elif (a_list[mid] > target):
      # item is less than the middle,
      # so we only need to look at the left
      # half of the current list
      return recursion(first, mid - 1)
    else:
      # found it!
      return mid

  return recursion(low, high)
