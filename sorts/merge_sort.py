def merge(left, right):
  result = []

  while left and right:
    if left[0] <= right[0]:
      result.append(left.pop(0))
    else:
      result.append(right.pop(0))

  return result + left + right

def merge_sort(lst):
  if len(lst) <= 1:
      return lst

  mid = len(lst) // 2

  left = merge_sort(lst[:mid])
  right = merge_sort(lst[mid:])

  return merge(left, right)
