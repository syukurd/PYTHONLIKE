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