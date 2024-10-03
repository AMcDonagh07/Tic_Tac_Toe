# Tic Tac Toe 03/10/2024

# Initialize the game board
board = [' ' for _ in range(9)]

# Function to display the board
def print_board():
    for row in [board[i:i + 3] for i in range(0, 9, 3)]:
        print('| ' + ' | '.join(row) + ' |')

# Function to check if a player has won
def check_winner(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                      (0, 4, 8), (2, 4, 6)]             # Diagonals
    return any(board[i] == board[j] == board[k] == player for i, j, k in win_conditions)

# Function to check if the board is full (draw)
def is_draw():
    return ' ' not in board

# Function to make a move
def make_move(player, position):
    if board[position] == ' ':
        board[position] = player
        return True
    return False

# Function to switch between players
def switch_player(current_player):
    return 'O' if current_player == 'X' else 'X'

# Main game loop
def tic_tac_toe():
    current_player = 'X'
    while True:
        print_board()
        
        # Get the player's move
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        
        # Ensure valid move
        if move < 0 or move > 8:
            print("Invalid move. Please enter a number between 1 and 9.")
            continue
        
        # Make the move
        if make_move(current_player, move):
            # Check for a win
            if check_winner(current_player):
                print_board()
                print(f"Player {current_player} wins!")
                break
            # Check for a draw
            if is_draw():
                print_board()
                print("It's a draw!")
                break
            # Switch player
            current_player = switch_player(current_player)
        else:
            print("That position is already taken. Try again.")

# Run the game
tic_tac_toe()
