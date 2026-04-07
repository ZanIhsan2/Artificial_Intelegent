import math

# Papan Tic-Tac-Toe (0-8)
board = [' ' for _ in range(9)]

# Fungsi untuk mencetak papan
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}\n")

# Cek apakah ada yang menang
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Vertical
        [0, 4, 8], [2, 4, 6]             # Diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Cek apakah papan penuh (Seri)
def is_board_full(board):
    return ' ' not in board

# ==========================================
# OTAK AI: ALGORITMA MINIMAX (Pemain O)
# ==========================================
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'): return 10 - depth
    if check_winner(board, 'X'): return -10 + depth
    if is_board_full(board): return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def minimax_move(board):
    best_score = -math.inf
    best_move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = 'O'
    print(f"🤖 Minimax (O) memilih petak {best_move}")

# ==========================================
# OTAK AI: ALGORITMA HILL CLIMBING (Pemain X)
# ==========================================
def hill_climbing_move(board):
    best_move = -1
    best_score = -math.inf
    
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            # Heuristik: 10 jika menang, 5 jika blokir lawan, 1 jika isi tengah, 0 sisanya
            if check_winner(board, 'X'):
                score = 10
            else:
                board[i] = ' ' # Undo simulasi X dulu
                board[i] = 'O' # Simulasi cek apakah lawan (O) akan menang
                if check_winner(board, 'O'):
                    score = 5
                else:
                    score = 1 if i == 4 else 0
            
            board[i] = ' ' # Undo simulasi
            
            if score > best_score:
                best_score = score
                best_move = i
    
    if best_move == -1:
        for i in range(9):
            if board[i] == ' ':
                best_move = i
                break

    board[best_move] = 'X'
    print(f"⛰️ Hill Climbing (X) memilih petak {best_move}")

# ==========================================
# MAIN LOOP
# ==========================================
print("Pertandingan AI: Hill Climbing (X) vs Minimax (O)\n")
print_board(board)

def pertandingan_ai():
    while True:
        # 1. Giliran Hill Climbing (X)
        hill_climbing_move(board)
        print_board(board)
        if check_winner(board, 'X'):
            print("Hill Climbing (X) Menang!")
            break
        if is_board_full(board):
            print("Seri!")
            break
            
        # 2. Giliran Minimax (O)
        minimax_move(board)
        print_board(board)
        if check_winner(board, 'O'):
            print("Minimax (O) Menang!")
            break
        if is_board_full(board):
            print("Seri!")
            break

minimax_win = 0
hill_climbing_win = 0
draw = 0

for i in range(10):
    board = [' ' for _ in range(9)]
    print(f"=== Pertandingan {i+1} ===")
    pertandingan_ai()
    if check_winner(board, 'X'):
        hill_climbing_win += 1
    elif check_winner(board, 'O'):
        minimax_win += 1
    else:
        draw += 1

print(f"\nHasil Akhir setelah 10 Pertandingan:")
print(f"Hill Climbing (X) Menang: {hill_climbing_win}")
print(f"Minimax (O) Menang: {minimax_win}")
print(f"Seri: {draw}")