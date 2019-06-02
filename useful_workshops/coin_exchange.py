def greedy_coin_change(amount, denoms):
  # how many denoms do we have to choose from
  n = len(denoms)

  # store a list that contains the number of
  # coins we need
  zeroes = [0] * n
  counts = [list(a) for a in zip(denoms, zeroes)]

  # traverse the list in reverse
  i = n - 1
  while i >= 0:
    # grab as many of the current coin as we can
    while amount >= denoms[i]:
      # we can fit one of these coins in, so:
      # remove the coin's value from the total
      amount -= denoms[i]

      # note that we've used one of these coins
      counts[i][1] += 1
    i -= 1

  # return the list of the number of coins
  return [tuple(a) for a in counts]

if __name__ == "__main__":
  target = int(input("Target amount ($): "))

  denoms = input("Denominations: ").split(",")
  denoms_lst = list(map(int, denoms))

  # 15, [1,7,13] --> [(1, 2), (7, 0), (13, 1)]
  print(greedy_coin_change(target, denoms_lst))
