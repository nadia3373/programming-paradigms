def print_board(board):
    for row in board:
        print(" ".join(row))

def check_winner(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        row = int(input(f"Игрок {current_player}, введите номер строки (1-3): ")) - 1
        col = int(input(f"Введите номер столбца (1-3): ")) - 1

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Игрок {current_player} победил!")
                break
            elif is_board_full(board):
                print_board(board)
                print("Ничья!")
                break

            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Некорректный ход. Повторите попытку.")

if __name__ == "__main__":
    play_game()
