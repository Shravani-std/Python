from random import randrange

def display_board(board):
    """Display the current state of the board."""
    print("+-------" * 3 + "+")
    for row in range(3):
        print("|   " + "   |   ".join(str(board[row][col]) for col in range(3)) + "   |")
        print("|       " * 3 + "|")
        print("+-------" * 3 + "+")

def enter_move(board):
    """Get the user's move and update the board."""
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9:
            move = int(move) - 1
            row = move // 3
            col = move % 3
            if board[row][col] not in ['O', 'X']:
                board[row][col] = 'O'
                return
            else:
                print("Field already occupied - try again!")
        else:
            print("Invalid input - enter a number between 1 and 9.")

def make_list_of_free_fields(board):
    """Return a list of all free positions on the board."""
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] not in ['O', 'X']]

def victory_for(board, sign):
    """Check if the given sign ('O' or 'X') has won."""
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],  # Top row
        [(1, 0), (1, 1), (1, 2)],  # Middle row
        [(2, 0), (2, 1), (2, 2)],  # Bottom row
        [(0, 0), (1, 0), (2, 0)],  # Left column
        [(0, 1), (1, 1), (2, 1)],  # Center column
        [(0, 2), (1, 2), (2, 2)],  # Right column
        [(0, 0), (1, 1), (2, 2)],  # Diagonal top-left to bottom-right
        [(0, 2), (1, 1), (2, 0)]   # Diagonal top-right to bottom-left
    ]
    for condition in win_conditions:
        if all(board[row][col] == sign for row, col in condition):
            return 'you' if sign == 'O' else 'me'
    return None

def draw_move(board):
    """Make a random move for the computer."""
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = free_fields[randrange(len(free_fields))]
        board[row][col] = 'X'

def tic_tac_toe():
    """Main function to play Tic-Tac-Toe."""
    board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
    board[1][1] = 'X'  # Computer's first move
    human_turn = True

    while make_list_of_free_fields(board):
        display_board(board)
        if human_turn:
            enter_move(board)
            victor = victory_for(board, 'O')
        else:
            draw_move(board)
            victor = victory_for(board, 'X')

        if victor:
            break

        human_turn = not human_turn

    display_board(board)
    if victor == 'you':
        print("You won!")
    elif victor == 'me':
        print("I won!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    tic_tac_toe()
