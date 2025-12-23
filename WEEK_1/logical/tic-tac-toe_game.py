import random 
# Function to print board
def print_board(board):
    for row in board:
        print(" |".join(row))
    print("-" * 5)

# function to check winner
def check_winner(board, mark):
    # check rows and columns
    for i in range(3):
        if all(board[i][j] == mark for j in range(3)): return True
        if all(board[j][i] == mark for j in range(3)): return True
        #check diagonals
        if all(board[i][i] == mark for i in range(3)): return True
        if all(board[i][2-i] == mark for i in range(3)): return True
        return False
    
# user move
def user_move(board):
    while True:
       row = int(input("enter row (0,2): "))
       col = int(input("enter column (0,2): "))
       if board[row][col] == " ":
           board[row][col] ="X"
           break
       else:
           print("cell already occupied!")

#computer move
def computer_move(board):
    while True:
        row,col = random.randint(0,2), random.randint(0,2)
        if board[row][col] == " ":
            board[row][col] == "O"
            print(f"computer chose:({row},{col})")
            break
    
# main game loop
def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    print_board(board)

    for turn in range(9):
        if turn % 2 == 0:
            user_move(board)
            print_board(board)
            if check_winner(board, "X"):
                print("User wins!")
                return
        else:
            computer_move(board)
            print_board(board)
            if check_winner(board, "O"):
                print("Computer wins!")
                return
    print("It's a draw!")

# run the game
tic_tac_toe()




