"""
untuk mendapatkan nomor acak seperti random, diperlukan untuk mengembalikan bilangan acak atau sama
dengan atau kurang dari

membuat fungsi dan x sebagai parameter sehingga kita bisa meneruskannya ke fungsi import random
"""

import random

def tebakan(x):
    nomor_acak = random.randint(1, x)
    tebakan = 0
    while tebakan != nomor_acak:
        tebakan = int(input(f'tebak angka antara 1 sampai {x}: '))
        if tebakan < nomor_acak:
            print('mahaf, tebakan ente terlalu rendah')
        elif tebakan > nomor_acak:
            print('mahaf, tebakan ente terlalu tinggi')

    print(f'selamet, ente menebak angka {nomor_acak} dan benar!!!')

tebakan(10)
