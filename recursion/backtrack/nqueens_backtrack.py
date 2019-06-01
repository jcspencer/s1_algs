def nqueens(n):
  # generate a blank n*n grid
  board = [[0] * n for _ in range(n)]
  # perform the algorithm on the board
  result = place(board, 0, len(board))

  if result:
    # result == True, so 'board' should
    # now contain a solution

    print('result found:')
    for row in board:
      # ints --> strings
      s = list(map(str, row))

      # print the row out, separated
      # by spaces
      print(' '.join(s))
  else:
    print('no result found.')

def safe(board, row, col):
  # move over every position
  for i in range(len(board)):
    for j in range(len(board)):
      if board[i][j] != 0:
        # horizontal collision
        if i == row:
          return False

        # vertical collision
        if j == col:
          return False

        # diagonal collision
        if abs(i - row) == abs(j - col):
          return False

  return True

def place(board, n, total):
  # we've hit the goal, break out
  # of the recursion
  if n >= total:
    return True

  # iterate over every piece
  for i in range(len(board)):
    for j in range(len(board)):
      # is this position safe?
      if safe(board, i, j):
        # try this move out
        board[i][j] = 1

        # continue down the chain
        if place(board, n+1, total):
          # if we get here, then we've solved
          # the n-queens problem, so we break
          # execution
          return True

        # if we're here,
        # move was not successful; we go back
        board[i][j] = 0

  # no solution was found
  return False

if __name__ == "__main__":
  nqueens(4)
