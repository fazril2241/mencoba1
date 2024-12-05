import random
from googlesearch import search

# Daftar dork umum yang bisa digunakan
dorks = {
    'SQL Injection': 'inurl:"?id=" inurl:"login"',
    'XSS': 'inurl:"<script>" inurl:"</script>"',
    'Admin Login': 'intitle:"admin login"',
    'File Upload': 'intitle:"file upload" inurl:"upload"',
    'Directory Traversal': 'inurl:"../" intitle:"index of"',
    'Login Bypass': 'inurl:"login" intitle:"login" "admin"',
}

# Fungsi untuk meminta input dari pengguna dan mencari dork
def google_dork():
    print("Google Dorking Script")
    print("=======================")
    
    # Menampilkan daftar dork yang tersedia
    print("Pilih jenis dork yang ingin dicari:")
    for idx, (key, value) in enumerate(dorks.items(), start=1):
        print(f"{idx}. {key}")

    # Meminta input dork dari pengguna
    dork_choice = int(input("Pilih nomor dork atau ketikkan dork kustom Anda: ").strip())

    if dork_choice <= len(dorks):
        # Mengambil dork berdasarkan pilihan pengguna
        dork = list(dorks.values())[dork_choice - 1]
    else:
        # Meminta dork kustom jika input tidak ada dalam daftar
        dork = input("Masukkan dork kustom Anda: ").strip()
    
    # Meminta jumlah hasil yang diinginkan
    num_results = int(input("Masukkan jumlah hasil yang diinginkan: ").strip())
    
    # Membuat query pencarian dengan dork
    query = f"{dork}"
    
    # Menampilkan hasil pencarian
    print(f"\nMencari: {query}")
    print(f"Mengambil {num_results} hasil...\n")
    
    try:
        # Melakukan pencarian di Google menggunakan modul 'googlesearch-python'
        results = search(query, num_results=num_results)

        # Menampilkan hasil pencarian
        for result in results:
            print(f"Found result: {result}")
    
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    google_dork()
