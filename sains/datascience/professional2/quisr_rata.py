# Dua buah data yang tersimpan dalam tipe list
data1 = [70, 70, 70, 100, 100, 100, 120, 120, 150, 150]
data2 = [50, 60, 60, 50, 70, 70, 100, 80, 100, 90]

def rata_rata(data) :
    jumlah = 0
    for i in data :
        jumlah += i
    rata_rata = jumlah/len(data)
    return rata_rata
print(rata_rata(data1))


def deviasi_rata(data) :
    rata_rata_devians = rata_rata(data)
    varians = 0
    for i in data :
        varians += (i - rata_rata_devians) ** 2
    varians /= len(data)    
    deviasi = varians ** (1/2)
    return deviasi

print (deviasi_rata(data2))