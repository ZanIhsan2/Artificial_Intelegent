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
# OTAK AI: ALGORITMA MINIMAX
# ==========================================
def minimax(board, depth, is_maximizing):
    # Base cases (Permainan Berakhir)
    if check_winner(board, 'O'): return 10 - depth  # AI menang (Makin cepat menang makin baik)
    if check_winner(board, 'X'): return -10 + depth # Manusia menang
    if is_board_full(board): return 0               # Seri

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O' # Simulasi AI jalan
                score = minimax(board, depth + 1, False)
                board[i] = ' ' # Undo simulasi
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X' # Simulasi Manusia jalan
                score = minimax(board, depth + 1, True)
                board[i] = ' ' # Undo simulasi
                best_score = min(score, best_score)
        return best_score

# Fungsi AI mengambil langkah
def ai_move(board):
    best_score = -math.inf
    best_move = 0
    
    print("🤖 AI sedang berpikir (mencoba semua kemungkinan)...")
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    
    board[best_move] = 'O'
    print(f"AI memilih petak nomor {best_move}")

# ==========================================
# MAIN LOOP (JALANKAN GAME)
# ==========================================
print("Selamat datang di Tic-Tac-Toe AI!")
print("Kamu adalah 'X' dan AI adalah 'O'. Petak bernomor 0-8 (Kiri atas ke Kanan Bawah).")
print_board(['0', '1', '2', '3', '4', '5', '6', '7', '8'])

while True:
    # Giliran Manusia
    move = int(input("Pilih petak kosong (0-8): "))
    if board[move] == ' ':
        board[move] = 'X'
    else:
        print("Petak sudah terisi!")
        continue
        
    print_board(board)
    if check_winner(board, 'X'):
        print("🎉 Kamu Menang! (Mustahil!)")
        break
    if is_board_full(board):
        print("🤝 Seri!")
        break
        
    # Giliran AI
    ai_move(board)
    print_board(board)
    if check_winner(board, 'O'):
        print("💀 AI Menang! Kamu kalah.")
        break
    if is_board_full(board):
        print("🤝 Seri!")
        break
def hill_climbing_move(board):
    print("⛰️ AI Hill Climbing sedang mencari langkah terbaik saat ini...")
    best_score = -math.inf
    best_move = -1
    
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            # Skor sederhana: 10 jika menang sekarang, 0 jika tidak
            score = 10 if check_winner(board, 'O') else 0
            board[i] = ' '
            
            if score > best_score:
                best_score = score
                best_move = i
                
    # Jika tidak ada langkah yang langsung menang, pilih langkah pertama yang tersedia
    if best_move == -1:
        for i in range(9):
            if board[i] == ' ': return i
            
    return best_move