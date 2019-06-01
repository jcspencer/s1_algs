def nqueens(n):
  board = [[0] * n for _ in range(n)]
  result = place(board, 0, len(board))

  if result:
    print('result found:')
    for row in board:
      s = list(map(str, row))
      print(' '.join(s))
  else:
    print('no result found.')

def safe(board, row, col):
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
  if n >= total:
    return True

  for i in range(len(board)):
    for j in range(len(board)):
      if safe(board, i, j):
        # try this move out
        board[i][j] = 1

        # continue down the chain
        if place(board, n+1, total):
          return True

        # move was not successful, go back
        board[i][j] = 0

  return False

if __name__ == "__main__":
  nqueens(8)
