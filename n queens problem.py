def is_safe(board, row, col, n):
    # Check left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(board, col, n):
    if col == n:
        return True

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_nqueens(board, col + 1, n):
                return True

            board[row][col] = 0  # Backtrack

    return False


# Main Program
n = int(input("Enter the value of N: "))

board = [[0 for _ in range(n)] for _ in range(n)]

if solve_nqueens(board, 0, n):
    print("\nSolution:")
    for row in board:
        print(*row)
else:
    print("No solution exists.")
