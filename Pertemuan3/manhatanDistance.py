# ============================================
# PRAKTIKUM: MENGHITUNG HEURISTIK ROBOT KURIR
# ============================================

def hitung_heuristik(titik_sekarang, titik_goal):
    """
    TUGAS KALIAN:
    Lengkapi fungsi ini menggunakan rumus Manhattan Distance!
    titik_sekarang = (x1, y1)
    titik_goal = (x2, y2)
    Gunakan fungsi abs() di Python untuk nilai absolut/positif.
    """
    x1, y1 = titik_sekarang
    x2, y2 = titik_goal

    # --- TULIS KODE KALIAN DI BAWAH INI ---
    h = abs(x1 - x2) + abs(y1 - y2)
    return h

# --- JANGAN UBAH KODE DI BAWAH INI ---
# Koordinat Titik Tujuan (Goal)
goal = (5, 5)

# Tiga pilihan jalan yang bisa diambil robot saat ini
pilihan_jalan = {
    "Titik A": (2, 4),
    "Titik B": (4, 1),
    "Titik C": (6, 5)
}

print(f"Target Goal berada di koordinat: {goal}\n")

# AI akan mengecek insting (heuristik) ke setiap pilihan jalan 
for nama_titik, koordinat in pilihan_jalan.items():
    h_value = hitung_heuristik(koordinat, goal)
    print(f"Jarak tebakan (Heuristik) dari {nama_titik} {koordinat} ke Goal adalah: {h_value}")

print("\nKESIMPULAN:")
print("Robot harus memilih titik dengan nilai Heuristik PALING KECIL!")