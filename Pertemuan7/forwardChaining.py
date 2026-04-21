# ==========================================
# PRAKTIKUM: LOGICAL AGENT (FORWARD CHAINING)
# ==========================================

print("🧠 Memulai Mesin Inferensi AI...\n")

# 1. KNOWLEDGE BASE (Basis Pengetahuan / Fakta Awal)
# Ini adalah memori AI atau data yang didapat dari sensor saat ini.
# Coba ganti-ganti isi set ini nanti! (Misal: {"Ada Angin"})
fakta_sensor_saat_ini = {"Ada Angin"}

# 2. RULE BASE (Buku Aturan Hukum Alam)
# Format: ( {Syarat 1, Syarat 2}, "Kesimpulan" )
aturan_wumpus_world = [
    ( {"Ada Bau Busuk"}, "Wumpus Dekat" ),
    ( {"Ada Angin"}, "Jurang Dekat" ),
    ( {"Wumpus Dekat", "Punya Panah"}, "Tembak Panah" ),
    ( {"Wumpus Dekat"}, "Bahaya Wumpus" ), # Aturan ini berlaku jika panah habis
    ( {"Jurang Dekat"}, "Mundur" ),
    ( {"Tidak Ada Angin", "Tidak Ada Bau"}, "Maju Aman" )
]

# 3. MESIN INFERENSI (Forward Chaining Algorithm)
def jalankan_inferensi(fakta, aturan):
    fakta_diketahui = fakta.copy()
    ada_fakta_baru = True
    putaran = 1
    
    print(f"📦 Fakta Awal: {fakta_diketahui}\n")
    
    # AI akan terus berpikir berputar-putar selama ia menemukan fakta baru
    while ada_fakta_baru:
        ada_fakta_baru = False
        print(f"--- Putaran Pemikiran Ke-{putaran} ---")
        
        # Cek setiap aturan di dalam buku aturan
        for syarat, kesimpulan in aturan:
            # Jika kesimpulan ini belum diketahui, DAN semua syaratnya terpenuhi oleh fakta saat ini
            if kesimpulan not in fakta_diketahui and syarat.issubset(fakta_diketahui):
                print(f"💡 Aha! Karena {syarat}, maka saya simpulkan: '{kesimpulan}'")
                
                # Masukkan kesimpulan baru ke dalam Otak AI
                fakta_diketahui.add(kesimpulan)
                ada_fakta_baru = True
                
        if not ada_fakta_baru:
            print("🛑 AI berhenti berpikir. Tidak ada kesimpulan baru yang bisa ditarik.\n")
            
        putaran += 1
        
    return fakta_diketahui
# --- JALANKAN PROGRAM ---
kesimpulan_akhir = jalankan_inferensi(fakta_sensor_saat_ini, aturan_wumpus_world)

print("📝 HASIL AKHIR ISI OTAK AI:")
for item in kesimpulan_akhir:
    print(f"- {item}")

# Eksekusi Keputusan Utama (Sistem Pakar Sederhana)
print("\n🤖 AKSI ROBOT SAAT INI:")
if "Tembak Panah" in kesimpulan_akhir:
    print(">>> 🏹 MENEMBAKKAN PANAH KE ARAH WUMPUS!")
elif "Mundur" in kesimpulan_akhir:
    print(">>> 🔙 BERBAHAYA! ROBOT MUNDUR 1 LANGKAH.")
elif "Maju Aman" in kesimpulan_akhir:
    print(">>> 🚶 ROBOT MAJU KE KOTAK SELANJUTNYA.")
else:
    print(">>> 🥶 ROBOT DIAM KETAKUTAN (Tidak ada aksi yang relevan).")