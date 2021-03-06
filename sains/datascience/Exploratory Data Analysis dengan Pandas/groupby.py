# Cobalah untuk mencari rata rata dari price per payment_type dari dataset order_df
#  ("https://storage.googleapis.com/dqlab-dataset/order.csv")!


import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
rata_rata = order_df["price"].groupby(order_df["payment_type"]).mean()
print(rata_rata)

# “Aksara, ini sudah menyeluruh dan lengkap. Tambahin satu lagi saja, tolong cari berapa harga maksimum pembelian customer di dataset order_df.”
# “Oke.”
sort_harga = order_df.sort_values("price",ascending=False)
print(sort_harga)