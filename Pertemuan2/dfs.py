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

# 1. Algoritma Breadth-First Search (DFS)
def dfs_search(graph, start, goal):
    visited = []      # Catatan jalan yang sudah dilewati
    stack = [start]   # Antrean pengecekan (Stack)

    print("Mulai penelusuran DFS:")
    while stack:
        # Ambil elemen TERAKHIR dari Last in 
        node = stack.pop() 

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
                    stack.append(tetangga)
                    
    print("Goal tidak ditemukan.")
    return visited

# --- JALANKAN PROGRAM ---
print("--- Hasil DFS ---")
dfs_hasil = dfs_search(graph, 'A', 'F')
print("Jalur DFS:", dfs_hasil)
print("\n")