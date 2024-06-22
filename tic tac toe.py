
board = [[' ' for _ in range(3)] for _ in range(3)]


def print_board():
    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("---+---+---")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("---+---+---")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])

def player_move(icon):
    if icon == 'X':
        number = 1
    elif icon == 'O':
        number = 2

    print(f"Player {number}, enter your move (row and column number, 0-2): ")
    row = int(input("Row: "))
    col = int(input("Column: "))

    if board[row][col] == ' ':
        board[row][col] = icon
    else:
        print("That space is taken! Try again.")
        player_move(icon)


def is_victory(icon):  
    for row in board:
        if row.count(icon) == 3:
            return True
    for col in range(3):
        if board[0][col] == icon and board[1][col] == icon and board[2][col] == icon:
            return True
    if board[0][0] == icon and board[1][1] == icon and board[2][2] == icon:
        return True
    if board[0][2] == icon and board[1][1] == icon and board[2][0] == icon:
        return True
    return False

def is_draw(board):
    if all(col != ' ' for row in board for col in row):
        return  True
    return False
while True:
    print_board()
    player_move('X')
    if is_victory('X'):
        print_board()
        print("Player 1 wins! Congratulations Expected!")
        break
    player_move('O')
    if is_victory('O'):
        print_board()
        print("Player 2 wins! Lucky you!")
        break

if all(col != ' ' for row in board for col in row):
    print("It's a tie!")

# Ask if players want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again =='yes':
       print("Thanks for playing!")