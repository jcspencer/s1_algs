def bounded_list(upper_bounds):
  first = len(upper_bounds) * [0]
  last = upper_bounds[:]
  res = [first]

  while res[-1] != last:
    res += [lex_suc(res[-1], last)]

  return res

# for a list 'lst' it holds that for all indices i, lst[i] ≤ upper_bounds[i]
def lex_suc(lst, last):
  res = lst[:] # make a copy of lst

  # traverse the list backwards,
  # beginning at the last element
  i = len(res) - 1
  while True:
    # if the condition holds...
    if res[i] < last[i]:
      # great! we can increase this column by one
      res[i] += 1

      # break out of the loop
      break
    else:
      # overflow! set this column to zero and
      # increase the next column (by recursing)
      res[i] = 0
      i -= 1

  # return the lexicographic successor
  return res

def multiply_sum(combo, denoms):
  # multiply each a[i] by b[i] and store it in c[i]
  multiplied = [a * b for a, b in zip(combo, denoms)]

  # return the sum of all the elements in c[i]
  return sum(multiplied)

def bruteforce_coin_exchange(amount, denominations):
  # upper bounds are calculated by how many times
  # the denomination fits in to the target (using floor division)
  bounds = list(map(lambda d: amount // d, denominations))

  # generate all combinations up to 'bounds'
  combinations = bounded_list(bounds)

  # hold possible solutions
  possible = []
  for combo in combinations:
    # total value of this combination
    total = multiply_sum(combo, denominations)

    # if the combo yields the amount we want
    if total == amount:
      # how many coins were used?
      coins = sum(combo)
      # append it to the list of possible combos
      possible.append([combo, coins])

  # order the list by amount of coins
  best_list = sorted(possible, key=lambda x: x[1])

  # get the combo with the least amount of coins used
  best_combo = best_list[0]

  # return the array of number of coins used
  return best_combo[0]

if __name__ == "__main__":
  print("test: bounded_list([1, 1, 2])")
  print(bounded_list([1, 2, 2]))
  print()

  print("test: bruteforce_coin_exchange(15, [1, 7, 13])")
  print(bruteforce_coin_exchange(15, [1, 7, 13]))
