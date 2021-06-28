nama_produk = "Sepatu Niko"
nama_produk = nama_produk[7:] + "P" + nama_produk [3:9] + "K" + nama_produk[-1]

print(nama_produk[:7])


# hitung jumlah jeruk
judul_artikel = [
"Buah Salak Baik untuk Mata", "Buah Salak Kaya Potasium", 
"Buah Jeruk Kaya Vitamin C", "Buah Salak Kaya Manfaat", 
"Salak Baik untuk Jantung", "Jeruk dapat Memperkuat Tulang", 
"Jeruk Mencegah Penyakit Asma", "Jeruk Memperkuat Gigi", 
"Jeruk Mencegah Kolesterol Jahat", "Salak Mencegah Diabetes", 
"Salak Memperkuat Dinding Usus", "Salak Baik untuk Darah",
"Jeruk Kaya Manfaat untuk Jantung", "Salak si Kecil yang Baik", 
"Jeruk dan Salak Buah Kaya Manfaat", "Buah Jeruk Enak",
"Tips Panen Jeruk Ribuan Kilo", "Tips Bertanam Salak", 
"Salak Manis untuk Berbuka", "Jeruk Baik untuk Wajah"
]

jeruk = 0
salak = judul_artikel.count("Salak")
for i in judul_artikel :
    if i.count("Jeruk") > 0 :
        jeruk += 1
print(jeruk) 
print(salak)



kata_positif = ["Kaya", "Baik", "Mencegah", "Memperkuat"]
jeruk_positif = 0
salak_positif = 0
for i in judul_artikel :
    for j in kata_positif :
        if i.count ("Jeruk") > 0 and i.count(j) :
            jeruk_positif += 1
        if i.count ("Salak") > 0 and i.count(j) :
            salak_positif += 1
print(jeruk_positif)
print(salak_positif)