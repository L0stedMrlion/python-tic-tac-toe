import json

def load_language(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def play_game():
    lang_file = "lang/eu.json"
    lang = load_language(lang_file)

    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    print(lang["welcome"])

    while True:
        print_board(board)

        player_prompt = lang["player_prompt"].format(players[current_player])
        move = input(player_prompt).split()

        if len(move) != 2 or not move[0].isdigit() or not move[1].isdigit():
            print(lang["invalid_move"])
            continue

        row, col = map(int, move)
        if not (0 <= row < 3) or not (0 <= col < 3) or board[row][col] != ' ':
            print(lang["invalid_move"])
            continue

        board[row][col] = players[current_player]

        if is_winner(board, players[current_player]):
            print_board(board)
            print(lang["game_over"].format(players[current_player]))
            break

        if is_board_full(board):
            print_board(board)
            print(lang["tie"])
            break

        current_player = 1 - current_player

if __name__ == "__main__":
    play_game()
