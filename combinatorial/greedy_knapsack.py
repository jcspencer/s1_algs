def greedy_items(values, weights, capacity):
  number = len(values)

  # zip up weights and values
  # makes an array of (w[i], v[i]) tuples
  weight_value = list(zip(weights, values))

  # 0 if not picked, 1 if picked
  best_combo = [0] * number
  weight = 0
  cost = 0

  # work out the value/weight ratios for each item
  ratios = []
  for idx, wc in enumerate(weight_value):
    (weight, value) = wc
    rat = value / weight
    ratios.append((idx, rat))

  # sort (index, ratio) by the ratio, in descending order
  ratios = sorted(ratios, key=lambda x: x[1], reverse=True)

  for index, ratio in ratios:
    # does this item fit in the bag?
    if weight_value[index][0] + weight <= capacity:
      # yes! add it to the total
      weight += weight_value[index][0]

      # increase the total cost
      cost += weight_value[index][1] # values[index]

      # note down that we picked it
      best_combo[index] = 1

  return best_combo, cost
