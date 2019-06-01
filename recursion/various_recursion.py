def fact(n):
  if n == 0:
    return 1
  else:
    return n * fact(n - 1)

def reverse(arr):
  # Move closer to the center from the outside,
  # swap pairs as we go along
  def reverser(arr, i, j):
    if i < j:
      # swap arr[i] and arr[j]
      arr[i], arr[j] = arr[j], arr[i]
      # move closer to the center
      i, j = i + 1, j - 1
      # recurse
      reverser(arr, i, j)

  cpy = arr.copy()
  reverser(cpy, 0, len(arr) - 1)
  return cpy

def simple_recursive_power(x, n):
  if n == 0:
    return 1
  else:
    return x * simple_recursive_power(x, n - 1)

def advanced_recursive_power(x, n):
  if n == 0:
    return 1
  elif n % 2 == 0:
    m = advanced_recursive_power(x, n / 2)
    return m * m
  else:
    return x * advanced_recursive_power(x, n - 1)
