# cardia  Riverlands  merupakan  tanah  yang  damai  sampai  Yu  Zhong  jelmaan  dari  Black
# Dragon datang dengan membawa 958.730 pasukan dan memporak-porandakan tempat
# tersebut. Mendengar berita atas kacaunya Cardia Riverlands, padepokan Dragon Altar
# mengirim  pahlawan  yang  terdiri  dari  Zilong,  Ling,  Baxia,  Wanwan,  dan  Chang’e  dengan
# misi  untuk  mengalahkan  semua  pasukan  Yu  Zhong.  Jika  para  pahlawan  Dragon  Altar
# bersepakat  untuk  membagi  musuh  sama  rata,  berapa  pasukan  yang  harus  dikalahkan  oleh
# setiap pahlawan Dragon Altar?
# Buatlah  program  untuk  menghitung  jumlah  pasukan  yang  harus  dikalahkan  oleh  setiap
# pahlawan Dragon Altar!

# Output → Note = tanda tanya “?” disesuaikan dengan soal
# Jumlah pasukan yang dibawa Yu Zhong = ?
# Jumlah pahlawan = ?
# Jumlah pasukan yang harus dikalahkan setiap pahlawan adalah 191746 pasukan

import math

total_enemy = 958730
total_heroes = 5
enemy_per_hero = total_enemy / total_heroes
print(f"Jumlah pasukan yang dibawa Yu Zhong = {total_enemy}")
print(f"Jumlah pahlawan = {total_heroes}")
print(
    f"Jumlah pasukan yang harus dikalahkan setiap pahlawan adalah {math.floor(enemy_per_hero)} pasukan"
)
