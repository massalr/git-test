"""
user akan memasukan input yang memiliki 3 pilihan berbeda gunting batu kertas dan komputer akan memilih secara acak
selanjutnya menentukan siapa yang menang menggunakan operator logika.
"""

import random

def mainkan():
    user = input("coba pilih, sob!! 'b' untuk batu, 'k' untuk kertas, 'g' untuk gunting\n")
    computer = random.choice(['b', 'k', 'g'])

    if user == computer:
        return 'ora ada yang menang'

# batu > gunting, gunting > kertas, kertas > batu
    if pemenang(user, computer):
        return 'ente menang sob'

    return 'ente kalah!!'

def pemenang(pemain, lawan):
    # return True apabila pemain menang
    # batu > gunting, gunting > kertas, kertas > batu
    if (pemain == 'b' and lawan == 'g') or (pemain == 's' and lawan == 'k') \
        or (pemain == 'k' and lawan == 'b'):
        return True

print(mainkan())