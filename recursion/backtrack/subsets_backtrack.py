def backtrack_subsets(output, last_combo, candidates, first_index):
  # use the fact that python uses list references
  # to populate the output list passed to the function
  output.append(last_combo)

  # go through the rest of the candidates
  for i in range(first_index, len(candidates)):
    # build the next combination
    next_combo = last_combo + [candidates[i]]

    # backtrack, increasing the starting index
    # for the candidates list
    backtrack_subsets(output, next_combo, candidates, i + 1)

def all_combinations(lst):
  subsets = []
  backtrack_subsets(subsets, [], lst, 0)

  return subsets
