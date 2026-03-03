# Representasi State Space dalam bentuk Dictionary
# Titik kiri adalah lokasi saat ini, titik kanan adalah cabang jalan yang bisa dilalui
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# 1. Algoritma Breadth-First Search (BFS)
def bfs_search(graph, start, goal):
    visited = []      # Catatan jalan yang sudah dilewati
    queue = [start]   # Antrean pengecekan (Queue)

    print("Mulai penelusuran BFS:")
    while queue:
        # Ambil elemen PERTAMA dari antrean (Indeks 0)
        node = queue.pop(0) 
        
        if node not in visited:
            print(f"Mengunjungi node: {node}")
            visited.append(node)
            
            # Jika goal ditemukan, berhenti
            if node == goal:
                print("🏁 GOAL DITEMUKAN!")
                return visited
            
            # Masukkan semua tetangga node ini ke dalam antrean
            for tetangga in graph[node]:
                if tetangga not in visited:
                    queue.append(tetangga)
                    
    print("Goal tidak ditemukan.")
    return visited

# --- JALANKAN PROGRAM ---
print("--- Hasil BFS ---")
bfs_hasil = bfs_search(graph, 'A', 'F')
print("Jalur BFS:", bfs_hasil)
print("\n")

# ==========================================
# TUGAS KALIAN:
# Buat fungsi dfs_search() di bawah ini!
# Clue: Ubah bagian 'queue.pop(0)' menjadi logika Stack (mengambil data TERAKHIR)
# ==========================================

# def dfs_search(graph, start, goal):
#     # Tulis kode kalian di sini...
