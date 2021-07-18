import matplotlib.pyplot as plt
import datetime
import pandas as pd
dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv')
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
dataset['CMV'] = dataset['item_price'] * dataset['quantity']
print(dataset.head())
plt.figure(figsize=(15,5))
a=dataset.groupby(['order_month'])['CMV'].sum().plot(linestyle='-.',marker='o',color='green',linewidth =2)
plt.title('Hello Dunia',loc='center',)
plt.xlabel('Order_month', fontsize=12)
plt.ylabel('Frekuensi', fontsize = 12) 
plt.grid(color = 'darkgray',linewidth = 0.5,linestyle = ':' )
labels,locations = plt.yticks()
plt.yticks(labels,(labels/1000000000).astype(int))
# netralkan batas maksimum dan minimum nilai axis ticks
plt.ylim(ymin = 0)
plt.text(0.45,0.72,'ini naik sedikit', color='red')

# simpan dalam bentuk png
plt.savefig('result.png',quality = 95)
# mengetahui apa saja format yang di dukung
# berbagai parameter yang bisa diatur saat menyimpan gambar, antara lain:

# dpi: Resolusi gambar (dots per inch). 
# quality: Kualitas gambar (hanya berlaku jika formatnya jpg atau jpeg), bisa diisi nilai 1 (paling buruk) hingga 95 (paling bagus).
# facecolor: Memberikan warna bagian depan figure, di luar area plot 
# edgecolor: Memberikan warna pinggiran gambar
# transparent: Jika nilainya True, maka gambarnya jadi transparan (jika filenya png)
 

plt.gcf().canvas.get_supported_filetypes()
plt.show()


