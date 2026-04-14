# ==========================================
# PRAKTIKUM: CSP MAP COLORING (BACKTRACKING)
# ==========================================

# 1. Definisi Peta (Tetangga)
# Contoh: 'Jawa' bertetangga dengan 'Sumatera' dan 'Kalimantan'
peta_stt_nf = {
    'Sumatera': ['Jawa'],
    'Jawa': ['Sumatera', 'Kalimantan'],
    'Kalimantan': ['Jawa', 'Sulawesi'],
    'Sulawesi': ['Kalimantan', 'Papua'],
    'Papua': ['Sulawesi']
}

# 2. Domain Warna yang tersedia
warna_tersedia = ['Merah', 'Hijau', 'Biru']

# 3. Fungsi untuk memeriksa apakah warna aman digunakan
def is_safe(wilayah, warna, assignment):
    for tetangga in peta_stt_nf[wilayah]:
        # Jika tetangga sudah punya warna dan warnanya sama, maka TIDAK AMAN
        if tetangga in assignment and assignment[tetangga] == warna:
            return False
    return True

# 4. Algoritma Backtracking CSP
def solve_csp(index_wilayah, wilayah_list, assignment):
    # Base Case: Jika semua wilayah sudah diberi warna
    if len(assignment) == len(wilayah_list):
        return assignment

    wilayah_skrg = wilayah_list[index_wilayah]

    # Coba setiap warna di Domain
    for warna in warna_tersedia:
        print(f"Mencoba warna {warna} untuk {wilayah_skrg}...")
        
        if is_safe(wilayah_skrg, warna, assignment):
            # Jika aman, simpan warna tersebut
            assignment[wilayah_skrg] = warna
            
            # Lanjut ke wilayah berikutnya
            hasil = solve_csp(index_wilayah + 1, wilayah_list, assignment)
            if hasil is not None:
                return hasil
            
            # BACKTRACK: Jika buntu, hapus warna dan coba warna lain di loop berikutnya
            print(f"⚠️ Mentok di {wilayah_skrg}, mundur (backtrack)...")
            del assignment[wilayah_skrg]

    return None

# --- JALANKAN PROGRAM ---
list_wilayah = list(peta_stt_nf.keys())
solusi = solve_csp(0, list_wilayah, {})
if solusi:
    print("\n✅ SOLUSI CSP DITEMUKAN:")
    for wilayah, warna in solusi.items():
        print(f"- {wilayah}: {warna}")
else:
    print("\n❌ Tidak ada solusi yang memenuhi batasan.")