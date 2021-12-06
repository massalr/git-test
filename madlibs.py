"""
terdapat beberapa string kosong yang akan di gabungkan menjadi sebuah kalimat,
string tersebut di isi menggunakan variable yang sudah di buat.
"""
putri_raja = input("putri raja: ")
pangeran = input("pangeran: ")
candi = input("candi: ")
jumlah = input("jumlah: ")

madlib = f"disebuah tempat seorang pangerang {pangeran} tergila2 dengan seorang putri bernama {putri_raja} \
    namun putri raja memberikan syarat untuk membuat {candi} sebanyak {jumlah}"

print("*"*100)
print("")
print(madlib)