def recursive_binary_search(a_list, target, low, high):
  a_list = sorted(a_list)

  def recursion(first, last):
      mid = (first + last) // 2
      if first > last:
          return None
      elif (a_list[mid] < target):
          return recursion(mid + 1, last)
      elif (a_list[mid] > target):
          return recursion(first, mid - 1)
      else:
          return mid

  return recursion(low, high)
