
def create_board():
    return ['1','2','3','4','5','6','7','8','9']

def print_board(board):
    print(f'''  {board[0]}  |  {board[1]}  |  {board[2]}
-----+-----+-----
  {board[3]}  |  {board[4]}  |  {board[5]}
-----+-----+-----
  {board[6]}  |  {board[7]}  |  {board[8]}
''')

def choose_symbol():
    symbol = input("choose X or O: ").upper()

    if symbol == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'

def get_move(board):
    move = input("choose a number between 1 and 9: ")
    if move.isdigit():
        move = int(move)
        if 1 <= move <= 9 and board[move - 1] not in ['X', 'O']:
            return move
    return None
def make_move(board, position, symbol):
    board[position - 1] = symbol

def check_winner(board, symbol):
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == symbol:
            return True

    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == symbol:
            return True

    if board[0] == board[4] == board[8] == symbol:
        return True
    if board[2] == board[4] == board[6] == symbol:
        return True
    return False

def is_tie(board):
    return all(x in ['X', 'O'] for x in board)

def switch_player(current_player, player_1, player_2):
    return player_2 if current_player == player_1 else player_1

def play_game():
    board = create_board()
    player_1, player_2 = choose_symbol()
    current_player = player_1

    while True:
        print_board(board)
        print(f"Player {current_player}, it's your turn")

        move = get_move(board)
        if move is None:
            print("Invalid move, try again")
            continue

        make_move(board, move, current_player)

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = switch_player(current_player, player_1, player_2)
play_game()
#ccc