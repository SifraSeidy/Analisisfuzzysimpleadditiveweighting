import numpy as np

# Fungsi untuk menghitung nilai preferensi
def hitung_nilai_preferensi(alternatif, kriteria, bobot):
    # Normalisasi matriks keputusan
    matriks_normalisasi = {}
    for alt, nilai in alternatif.items():
        normalisasi = []
        for i in range(len(kriteria)):
            min_value = min([alternatif[a][i] for a in alternatif])
            max_value = max([alternatif[a][i] for a in alternatif])
            if max_value - min_value == 0:
                normalisasi.append(0)
            else:
                normalisasi.append((nilai[i] - min_value) / (max_value - min_value))
        matriks_normalisasi[alt] = normalisasi

    # Menghitung nilai preferensi
    nilai_preferensi = {}
    for alt, normalisasi in matriks_normalisasi.items():
        nilai_preferensi[alt] = np.dot(normalisasi, bobot)

    return nilai_preferensi

    # Memanggil fungsi untuk menghitung nilai preferensi
    hasil_preferensi = hitung_nilai_preferensi(alternatif, kriteria, bobot)