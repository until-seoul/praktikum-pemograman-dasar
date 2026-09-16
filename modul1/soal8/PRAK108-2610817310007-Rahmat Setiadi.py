# Hari ini Pak Dengklek jogging mengelilingi taman berbentuk  lingkaran sebanyak 5 putaran.
# Berdasarkan  aplikasi  Runkeeper  pada  smartphone  yang  digunakan,  Pak  Dengklek  telah
# berlari sejauh 14 kilometer. Berapakah jari-jari taman yang dikelilingi Pak Dengklek?

# Output
# Diketahui :
# Pak Dengklek mengelilingi taman = 5 Putaran
# Jarak tempuh Pak Dengklek = 14 Kilometer

# Jawaban :
# Jari-jari taman yang dikelilingi Pak Dengklek adalah 0.45 Kilometer

import math

# Diketahui
putaran = 5
jarak_tempuh = 14  # kilometer

# Menghitung keliling taman
keliling = jarak_tempuh / putaran

# Menghitung jari-jari taman
jari_jari = keliling / (2 * math.pi)

# Menampilkan hasil
print("Diketahui :")
print("Pak Dengklek mengelilingi taman =", putaran, "Putaran")
print("Jarak tempuh Pak Dengklek =", jarak_tempuh, "Kilometer")
print("\nJawaban :")
print(f"Jari-jari taman yang dikelilingi Pak Dengklek adalah {jari_jari:.2f} Kilometer")
