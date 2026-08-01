board = [[" "]*7 for i in range(6)]

def display():
    for row in board:
        print(row)

def drop(col, piece):
    for row in range(5,-1,-1):
        if board[row][col]==" ":
            board[row][col]=piece
            break

drop(3,"R")
drop(3,"B")
drop(2,"R")
drop(4,"B")
drop(1,"R")

display()

print("Minimax algorithm is used in Connect Four AI.")
