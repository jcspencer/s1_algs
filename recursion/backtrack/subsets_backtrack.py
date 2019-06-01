def backtrack_subsets(output, last_combo, candidates, first_index):
  output.append(last_combo)

  for i in range(first_index, len(candidates)):
    next_combo = last_combo + [candidates[i]]

    backtrack_subsets(output, next_combo, candidates, i + 1)

def all_combinations(lst):
  subsets = []
  backtrack_subsets(subsets, [], lst, 0)

  return subsets
