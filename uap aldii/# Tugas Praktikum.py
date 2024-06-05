import matplotlib.pyplot as plt

# Data nilai-nilai ujian mahasiswa
nilai_mahasiswa = [75, 80, 90, 65, 70, 85, 95, 78, 88, 92]

# Menghitung rata-rata
rata_rata = sum(nilai_mahasiswa) / len(nilai_mahasiswa)

# Membuat label mahasiswa (sumbu x)
label_mahasiswa = [f'Mahasiswa-{i+1}' for i in range(len(nilai_mahasiswa))]

# Visualisasi data dalam bentuk diagram batang
plt.bar(label_mahasiswa, nilai_mahasiswa)
plt.xlabel('Mahasiswa')
plt.ylabel('Nilai Ujian')
plt.title('Diagram Batang Nilai Ujian Mahasiswa')

# Menampilkan rata-rata pada diagram
plt.axhline(y=rata_rata, color='r', linestyle='-', label=f'Rata-rata: {rata_rata:.2f}')

# Menambahkan label dan legend
plt.legend()
plt.show()

print(f"Rata-rata nilai ujian mahasiswa: {rata_rata:.2f}")
