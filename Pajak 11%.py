# Menghitung total pembayaran
def hitung_total_pembayaran(nilai_pembelian):
    pajak = 0.11  # 11% pajak
    total_pembayaran = nilai_pembelian + (nilai_pembelian * pajak)
    return total_pembayaran

# Input
try:
    nilai_pembelian = float(input("Masukkan nilai pembelian: "))
    if nilai_pembelian < 0:
        print("Nilai pembelian tidak boleh negatif.")
    else:
        total = hitung_total_pembayaran(nilai_pembelian)
        print(f"Total yang harus dibayar setelah pajak adalah: {total:.2f}")
except ValueError:
    print("Input tidak valid. Harap masukkan angka yang valid.")