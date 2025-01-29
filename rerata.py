# List
nilai = []

# Input
for i in range(10):
    while True:
        try:
            angka = float(input(f"Masukkan nilai ke-{i + 1}: "))
            nilai.append(angka)
            break
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

# Menghitung rata-rata
rata_rata = sum(nilai) / len(nilai)

# Output
print("Rata-rata dari nilai yang dimasukkan adalah:", rata_rata)