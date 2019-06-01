# BEST CASE: O(nlogn)
# WORST CASE: O(nlogn)
def merge_sort(lst):
  # don't sort if list is already
  # sorted
  if len(lst) <= 1:
      return lst

  # get the 'middle' index in the list
  mid = len(lst) // 2

  # sort the left and right sides
  # recursively
  left = merge_sort(lst[:mid])
  right = merge_sort(lst[mid:])

  # merge the two sorted halves
  return merge(left, right)

def merge(left, right):
  result = []

  # while both sides have stuff in them
  while left and right:
    if left[0] <= right[0]:
      # if first item on left is smaller,
      # pop it off and add it to the result
      result.append(left.pop(0))
    else:
      # if first item on right is smaller,
      # pop it off and add it to the result
      result.append(right.pop(0))

  # gather the remaining stuff
  return result + left + right

if __name__ == "__main__":
  print(merge_sort([5,4,3,2,1]))
