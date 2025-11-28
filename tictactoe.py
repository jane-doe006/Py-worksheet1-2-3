board = [' ' for _ in range(9)]

def print_board():
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_win(player_icon):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player_icon:
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player_icon:
            return True
    
    if board[0] == board[4] == board[8] == player_icon:
        return True
    if board[2] == board[4] == board[6] == player_icon:
        return True
    return False

def check_draw():
    return ' ' not in board

def play_game():
    current_player = 'X'
    game_over = False

    while not game_over:
        print_board()
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if not (0 <= move <= 8) or board[move] != ' ':
                print("Invalid move. Please choose an empty space between 1 and 9.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        board[move] = current_player

        if check_win(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            game_over = True
        elif check_draw():
            print_board()
            print("It's a draw!")
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'
play_game()