import random
from googlesearch import search

# Daftar beberapa file type untuk dorking
file_types = ['pdf', 'txt', 'html', 'csv', 'sql']

# Fungsi untuk meminta input dari pengguna dan mencari dork
def google_dork():
    print("Google Dorking Script")
    print("=======================")
    
    # Meminta input dari pengguna
    dork = input("Masukkan dork yang ingin dicari (misalnya: inurl:login, intitle:admin, dll): ").strip()
    num_results = int(input("Masukkan jumlah hasil yang diinginkan: ").strip())
    
    # Pilih file types untuk pencarian (jika diperlukan)
    print("Pilih file type untuk pencarian (contoh: pdf, txt, html, dll):")
    for i, file_type in enumerate(file_types):
        print(f"{i+1}. {file_type}")
    file_choice = int(input("Pilih nomor file type: ").strip())
    
    selected_file_type = file_types[file_choice - 1]
    
    # Membuat query pencarian dengan dork dan file type
    query = f"{dork} filetype:{selected_file_type}"
    
    # Menampilkan hasil pencarian
    print(f"\nMencari: {query}")
    print(f"Mengambil {num_results} hasil...\n")
    
    try:
        # Melakukan pencarian di Google menggunakan modul 'googlesearch-python'
        # Menggunakan 'num_results' untuk menentukan jumlah hasil yang diambil
        results = search(query, num_results=num_results)
        
        # Menampilkan hasil pencarian
        for result in results:
            print(f"Found result: {result}")
    
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    google_dork()
