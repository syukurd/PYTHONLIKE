import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()
x_label = table['NAMA KELURAHAN']
plt.bar(x=np.arange(len(x_label)),height=table['LAKI-LAKI WNI'])
plt.xticks(np.arange(len(x_label)),x_label,rotation = 20)
plt.xlabel('Keluarahan di Jakarta pusat')
plt.ylabel('Jumlah Penduduk Laki - Laki')
plt.title('Persebaran Jumlah Penduduk Laki- Laki di Jakarta Pusat')
plt.show()


print(table.columns) #menampilkan column
print(table['Age']) #menampilkan isi dari age
print(table.iloc[5]) #menampilkan isi dari baris
print(table['Age'].iloc[1]) #menampilkan isi baris 1 dan column age
print(table['Age'].iloc[5:10])#menampilkan isi baris 5-10 dan column age
print(table.describe(include='all')) #menampilkan gambaran data keseluruhan ini strig masuk kedalam dan mnghasilkan banyak output Nan
print(table.describe(exclude=['O'])) #menampilkan gambaran data keseluruhan dengan memfilter yang bernilai string

#MELAKUKAN MISSING VALUES -> TRACE(RECORD ULANG DATA)
print(table.isnull().values.any()) #menampilkan data yang datanya kosong(null/nan)
print(table.mean()) #melakukan rata-rata
print(table.head(10)) #menampilkan sepuluh data yang ada nan atau null

table = table.fillna(table.mean()) #mengisi data yang kosong dengan perhitungan rata2 dalam data
print(table.head(10)) #menampilkan sepuluh data yang terisi dengan fillna