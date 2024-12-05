import random
from googlesearch import search


dorks = {
    'SQL Injection': 'inurl:"?id=" inurl:"login"',
    'XSS': 'inurl:"<script>" inurl:"</script>"',
    'Admin Login': 'intitle:"admin login"',
    'File Upload': 'intitle:"file upload" inurl:"upload"',
    'Directory Traversal': 'inurl:"../" intitle:"index of"',
    'Login Bypass': 'inurl:"login" intitle:"login" "admin"',
}


def google_dork():
    print("Google Dorking Script")
    print("=======================")
    
    
    print("Pilih jenis dork yang ingin dicari:")
    for idx, (key, value) in enumerate(dorks.items(), start=1):
        print(f"{idx}. {key}")

    
    dork_choice = int(input("Pilih nomor dork atau ketikkan dork kustom Anda: ").strip())

    if dork_choice <= len(dorks):
        
        dork = list(dorks.values())[dork_choice - 1]
    else:
        
        dork = input("Masukkan dork kustom Anda: ").strip()
    
    
    num_results = int(input("Masukkan jumlah hasil yang diinginkan: ").strip())
    
    
    query = f"{dork}"
    
    
    print(f"\nMencari: {query}")
    print(f"Mengambil {num_results} hasil...\n")
    
    try:
        
        results = search(query, num_results=num_results)

        
        for result in results:
            print(f"Found result: {result}")
    
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    google_dork()
